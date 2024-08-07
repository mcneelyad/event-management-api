from datetime import datetime
from typing import Optional
from pydantic import Field

from src.schemas.base_schema import BaseSchema

class EventSchema(BaseSchema):
    id: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    location: Optional[str] = Field(None)
    price: float
    capacity: int
    is_active: bool
    is_online: bool