from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomCreate(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str]

    @validator('name')
    def name_is_not_null(cls, value: str):
        if not value:
            return ValueError('Имя не может быть пустым')
        return value
