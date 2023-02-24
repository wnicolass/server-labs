from enum import Enum
from pydantic import BaseModel, Field

class PlayerBase(BaseModel):
    full_name: str
    email: str

class PlayerRegister(PlayerBase):
    password: str
    phone_number: str | None = Field(
        title="Local portuguese phone number or international prefixed w/ +XYZ country code"
    )
    birth_date: str | None
    level: str
    tournament_id: int | None

class PlayerRegisterResult(PlayerBase):
    id: int