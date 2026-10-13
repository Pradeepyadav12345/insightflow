from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.models.models import Organization, Role, User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse
from app.security.auth import create_access_token, get_current_user, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse)
def register_user(payload: RegisterRequest, db: Session = Depends(get_db)) -> TokenResponse:
    email = payload.email.lower()
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    organization = db.query(Organization).filter(Organization.slug == "default").first()
    if organization is None:
        organization = Organization(
            name=payload.organization_name or "Default Organization",
            slug="default",
        )
        db.add(organization)
        db.flush()

    role = db.query(Role).filter(Role.name == "ADMIN").first()
    if role is None:
        role = Role(name="ADMIN", description="Default admin role")
        db.add(role)
        db.flush()

    user = User(
        email=email,
        full_name=payload.full_name,
        hashed_password=hash_password(payload.password),
        organization_id=organization.id,
        role_id=role.id,
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(user.email, str(organization.id))
    return TokenResponse(access_token=token, token_type="bearer", expires_in_minutes=settings.jwt_access_token_expire_minutes)


@router.post("/login", response_model=TokenResponse)
def login_user(payload: LoginRequest, db: Session = Depends(get_db)) -> TokenResponse:
    user = db.query(User).filter(User.email == payload.email.lower()).first()
    if not user or not user.hashed_password or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is inactive")

    token = create_access_token(user.email, str(user.organization_id) if user.organization_id else None)
    return TokenResponse(access_token=token, token_type="bearer", expires_in_minutes=settings.jwt_access_token_expire_minutes)


@router.get("/me", response_model=UserResponse)
def get_current_user_profile(current_user: User = Depends(get_current_user)) -> UserResponse:
    organization_name = current_user.organization.name if current_user.organization else None
    role_name = current_user.role.name if current_user.role else None

    return UserResponse(
        id=str(current_user.id),
        email=current_user.email,
        full_name=current_user.full_name,
        organization_name=organization_name,
        role=role_name,
    )
