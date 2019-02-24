from datetime import date
from calendar import monthrange

WEEKDAYS = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
INDEXES = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4, "last": -1}


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, weekday, prefix):
    start_weekday, number_of_days = monthrange(year, month)
    monthdays = [monthday for monthday in range(number_of_days) if (monthday + start_weekday) % 7 == WEEKDAYS[weekday]]
    INDEXES["teenth"] = 2 if monthdays[0] in range(5) else 1
    if INDEXES[prefix] + 1 > len(monthdays):
        raise MeetupDayException("You entered wrong parameters")
    return date(year, month, monthdays[INDEXES[prefix]] + 1)
