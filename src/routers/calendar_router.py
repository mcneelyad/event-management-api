from fastapi import APIRouter

from src.services import calendar_service
from src.schemas.calendars.calendars_schema import CreateCalendarSchema

router = APIRouter(tags=["calendars"])

@router.get("/")
def get_all_calendars():
    return {"message": "This will return all calendars"}

@router.get("/{calendar_id}")
def get_calendar(calendar_id: int):
    return calendar_service.get_calendar(calendar_id)

@router.post("/")
def create_calendar(create_calendar: CreateCalendarSchema):
    return calendar_service.create_calendar(create_calendar)

@router.put("/{calendar_id}")
def update_calendar(calendar_id: int):
    return {"message": f"This will update calendar with id {calendar_id}"}

@router.delete("/{calendar_id}")
def delete_calendar(calendar_id: int):
    return {"message": f"This will delete calendar with id {calendar_id}"}