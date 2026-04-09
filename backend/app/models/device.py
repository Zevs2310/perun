from pydantic import BaseModel

class Device(BaseModel):
    id: int
    hostname: str
    ip: str
    status: str
    owner: str
