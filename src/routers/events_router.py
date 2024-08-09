from fastapi import APIRouter

from src.services import event_service
from src.schemas.events.events_schema import CreateEventSchema

router = APIRouter(tags=["events"])

@router.get("/")
def get_all_events():
    return {"message": "This will return all events"}

@router.get("/{event_id}")
def get_event(event_id: int):
    return event_service.get_event(event_id)

@router.post("/")
def create_event(create_event: CreateEventSchema):
    return event_service.create_event(create_event)

@router.put("/{event_id}")
def update_event(event_id: int):
    return event_service.update_event(event_id)

@router.delete("/{event_id}")
def delete_event(event_id: int):
    return {"message": f"This will delete event with id {event_id}"}