from src.schemas.events.events_schema import EventSchema

def get_event(event_id: int):
    return {"message": f"This will return event with id {event_id}"}

def create_event(event: EventSchema):
    return {"message": f"This will create a new event with name {event.name}"}