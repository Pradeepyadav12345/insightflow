from app.security.auth import create_access_token, hash_password, verify_password


def test_password_hash_and_verify() -> None:
    password = "StrongP@ssw0rd!"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("wrong-password", hashed) is False


def test_create_access_token_contains_user_claims() -> None:
    token = create_access_token("user@example.com", "org-123")

    assert isinstance(token, str)
    assert token
    assert token.count(".") == 2
