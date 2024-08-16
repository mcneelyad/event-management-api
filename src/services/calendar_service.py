from src.repositories import calendar_repository

def get_all_calendars():
    return calendar_repository.get_all_calendars()

def get_calendar(calendar_id: int):
    return calendar_repository.get_calendar(calendar_id)

def create_calendar(create_calendar):
    return calendar_repository.create_calendar(create_calendar)