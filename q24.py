""" question-24 """
import datetime


def solve(input_list):
    """This function return weekday of given date

    Parameters:
        tuple of yyyy mm dd

    Returns:
        string: weekday
    """
    (year, month, date) = input_list
    weekdays_mapping = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    datetime_instance1 = datetime.date(year, month, date)
    return weekdays_mapping[datetime_instance1.weekday()]


print("today's date: ", solve((2023, 10, 6)))
