""" question-25 """
import calendar
from datetime import datetime


def month_number(month):
    """return month number from string input"""
    month_calendar = {month: index for index, month in enumerate(calendar.month_abbr)}
    return month_calendar[month]


def solve(input_list):
    """This function return weekday of given date

    Parameters:
        tuple of yyyy mm dd

    Returns:
        string: weekday
    """
    time_stamp = []
    for times in input_list:
        [_, day, month, year, hms, tz] = times.split(" ")
        # removing preceding zro from day number
        if day[0] == "0":
            day = day[1:]
        # converting giving time to date data type from string
        date_str = f"{year}-{month_number(month)}-{day} {hms} {tz}"
        date_format = "%Y-%m-%d %H:%M:%S %z"
        date_obj = int(datetime.strptime(date_str, date_format).timestamp())
        time_stamp.append(date_obj)

    return time_stamp[0] - time_stamp[1]


print(
    "today's date: ",
    solve(["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"]),
)
