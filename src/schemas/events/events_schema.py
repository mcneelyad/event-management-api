from datetime import datetime, timedelta
from typing import Optional
from pydantic import Field

from src.schemas.base_schema import BaseSchema

class EventSchema(BaseSchema):
    id: int
    name: str
    description: str
    start_date: datetime = Field(datetime.now())
    end_date: datetime = Field(datetime.now() + timedelta(hours=2))
    location: Optional[str] = Field(None)
    price: float
    capacity: int
    is_active: bool = Field(True)
    is_online: bool

class CreateEventSchema(BaseSchema):
    name: str
    description: str
    start_date: datetime = Field(datetime.now())
    end_date: datetime = Field(datetime.now() + timedelta(hours=2))
    location: Optional[str] = Field(None)
    price: float
    capacity: int
    is_online: bool