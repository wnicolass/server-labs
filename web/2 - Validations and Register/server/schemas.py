from enum import Enum
from pydantic import BaseModel, Field

class PlayerBase(BaseModel):
    full_name: str
    email: str

    class Config:
        orm_mode = True

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

class TournamentBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class TournamentRegister(TournamentBase):
    start_date: str
    end_date: str

class TournamentRegisterResult(TournamentBase):
    id: int

class ErrorCode(Enum):
    ERR_UNSPECIFIED_TOURNAMENT = 'Missing tournament id.'
    ERR_PLAYER_ALREADY_ENROLLED = 'Player already enrolled in tournament'
    ERR_UNKNOWN_TOURNAMENT_ID = 'Unknown tournament id'
    ERR_NO_TOURNAMENT_AVAILABLE = 'No tournament available'
    ERR_TOURNAMENT_ALREADY_EXISTS = 'Tournament already exists.'

    def details(self, **kargs) -> dict:
        details_dict = {'error_code': self.name, 'error_msg': self.value}
        details_dict.update(kargs)
        return details_dict