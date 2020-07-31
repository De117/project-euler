# Problem 19
# ==========
#
# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
from datetime import datetime


def calculate_weekday(year, month, day):
    """Return 0-6, for Mondays-Sundays respectively"""

    def is_leap_year(year: int):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        return False

    def month_length(year: int, month: int):
        if month == 2:
            return 28 + is_leap_year(year)
        elif month in (4,6,9,11):
            return 30
        else:
            return 31

    d_years = (year - 1900) * 365 + sum(is_leap_year(y) for y in range(1900, year))
    d_months = sum(month_length(year, m) for m in range(1, month))

    d_total = d_years + d_months + (day - 1)

    return d_total % 7  # Mondays are 0


if __name__ == "__main__":
    sundays = 0
    for year in range(1901, 2000+1):
        for month in range(1, 12+1):
            weekday = calculate_weekday(year, month, 1)
            assert weekday == datetime(year, month, 1).weekday()  # Check with stdlib
            if weekday == 6:
                sundays += 1
    print(sundays)
