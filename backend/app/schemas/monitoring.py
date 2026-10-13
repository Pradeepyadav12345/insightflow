from pydantic import BaseModel


class SystemHealthResponse(BaseModel):
    status: str
    services: dict
    timestamp: str
