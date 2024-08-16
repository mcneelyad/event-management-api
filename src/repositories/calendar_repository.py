from src.repositories.database import get_database

def get_all_calendars():
    try:
        db = get_database()
        query = "SELECT * FROM calendars"
        calendars = db.execute(query)
        db.close()
        return calendars
    except Exception as e:
        raise e

def get_calendar(calendar_id: int):
    try:
        db = get_database()
        query = "SELECT * FROM calendars WHERE id = %s"
        values = (calendar_id,)
        calendar = db.execute(query, values)
        db.close()
        return calendar
    except Exception as e:
        raise e

def create_calendar(create_calendar):
    try:
        db = get_database()
        query = "INSERT INTO calendars (name, visibility) VALUES (%s, %s)"
        values = (create_calendar.name, create_calendar.visibility)
        db.execute(query, values)
        db.commit()
        db.close()
        return {"message": f"Calendar {create_calendar.name} created successfully"}
    except Exception as e:
        raise e