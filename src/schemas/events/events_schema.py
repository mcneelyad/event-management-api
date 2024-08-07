from datetime import datetime
import uuid

from src.schemas.base_schema import BaseSchema

class EventSchema(BaseSchema):
    id: uuid.UUID
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    location: str
    price: float
    capacity: int
    is_active: bool
    is_online: bool