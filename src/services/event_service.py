from src.schemas.events.events_schema import CreateEventSchema, EventSchema
from src.repositories import event_repository

def get_event(event_id: int):
    try:
        event = event_repository.get_event(event_id)
        return event
    except Exception as e:
        return str(e)

def create_event(event: CreateEventSchema):
    if event.is_online:
        event.location = None
    new_event_id = event_repository.create_event(event)
    return { "message": f"Event created successfully with id {new_event_id}" }

def update_event(event: EventSchema):
    if not event_repository.get_event(event.id):
        return { "message": f"Event with id {event.id} not found" }
    return event_repository.update_event(event)

def delete_event(event_id: int):
    if not event_repository.get_event(event_id):
        return { "message": f"Event with id {event_id} not found" }
    return event_repository.delete_event(event_id)