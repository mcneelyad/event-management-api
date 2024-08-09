from src.repositories.database import get_database
from src.schemas.events.events_schema import CreateEventSchema, EventSchema

def create_event(event: CreateEventSchema):
    database = get_database()
    try:
        query = "INSERT INTO events (name, description, start_date, end_date, location, price, capacity, is_online) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        values = (event.name, event.description, event.start_date, event.end_date, event.location, event.price, event.capacity, event.is_online)
        database.execute(query, values)
        database.commit()
        event_id = database.cursor.lastrowid
        return event_id
    except Exception as e:
        return str(e)
    finally:
        database.close()

def get_event(event_id: int):
    database = get_database()
    try:
        query = "SELECT * FROM events WHERE id = %s;"
        values = (event_id,)

        database.cursor.execute(query, values)

        event = database.cursor.fetchone()
        if not event:
            raise Exception(f"Event with id {event_id} not found")

        return EventSchema(
        id=event[0],
        name=event[1],
        description=event[2],
        start_date=event[3],
        end_date=event[4],
        location=event[5],
        price=event[6],
        capacity=event[7],
        is_active=event[8],
        is_online=event[9]
    )
    except Exception as e:
        return str(e)

def update_event(event: EventSchema):
    try:
        database = get_database()
        query = "UPDATE events SET name = %s, description = %s, start_date = %s, end_date = %s, location = %s, price = %s, capacity = %s, is_online = %s WHERE id = %s;"
        values = (event.name, event.description, event.start_date, event.end_date, event.location, event.price, event.capacity, event.is_online, event.id)
        database.execute(query, values)
        database.commit()
        return event.id
    except Exception as e:
        return str(e)
    finally:
        database.close()

def delete_event(event_id: int):
    database = get_database()
    query = "DELETE FROM events WHERE id = %s;"
    values = (event_id,)
    database.execute(query, values)
    database.commit()
    return event_id