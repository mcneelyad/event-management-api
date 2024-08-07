from fastapi import APIRouter

from src.services import event_service
from src.schemas.events.events_schema import EventSchema

router = APIRouter(tags=["events"])

@router.get("/")
def get_all_events():
    return {"message": "This will return all events"}

@router.get("/{event_id}")
def get_event(event_id: int):
    return event_service.get_event(event_id)

@router.post("/")
def create_event(create_event: EventSchema):
    return event_service.create_event(create_event)