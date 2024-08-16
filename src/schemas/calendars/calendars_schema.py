from typing import Literal
from src.schemas.base_schema import BaseSchema

class CreateCalendarSchema(BaseSchema):
    name: str
    visibility: str = Literal["public", "private"]
    is_active: bool = True

class CalendarSchema(CreateCalendarSchema):
    id: int

class CalendarEventSchema(BaseSchema):
    calendar_id: int
    event_id: int
    is_active: bool = True