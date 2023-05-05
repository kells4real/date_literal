# Returns more accurate readings
from datetime import datetime


def date_time_diff(time1, time2, time_='s'):
    dt1 = datetime.fromisoformat(time1.replace('Z', '+00:00'))
    dt2 = datetime.fromisoformat(time2.replace('Z', '+00:00'))
    result = (dt1 - dt2).total_seconds()

    if time_ == 'm' or time_ == 'M':
        return round(result / 60, 2)
    elif time_ == 'h' or time_ == 'H':
        return round(result / 3600, 2)
    elif time_ == 'd' or time_ == 'D':
        return round(result / 86400, 2)
    else:
        return result


def date_diff(date1, date2, time_unit='s'):
    datetime1 = datetime.fromisoformat(str(date1))
    datetime2 = datetime.fromisoformat(str(date2))

    diff = datetime1 - datetime2

    if time_unit == 'm' or time_unit == 'M':
        return round(diff.total_seconds() / 60, 2)
    elif time_unit == 'h' or time_unit == 'H':
        return round(diff.total_seconds() / 3600, 2)
    elif time_unit == 'd' or time_unit == 'D':
        return round(diff.days, 2)
    else:
        return round(diff.total_seconds(), 2)


CONVERSION_FACTORS = {
    "Y": {"W": 365 / 7, "D": 365, "H": 365 * 24, "M": 365 * 24 * 60, "S": 365 * 24 * 60 * 60},
    "W": {"Y": 1 / 52.18, "D": 7, "H": 7 * 24, "M": 7 * 24 * 60, "S": 7 * 24 * 60 * 60},
    "D": {"Y": 1 / 365, "W": 1 / 7, "H": 24, "M": 24 * 60, "S": 24 * 60 * 60},
    "H": {"Y": 1 / (365 * 24), "W": 1 / (7 * 24), "D": 1 / 24, "M": 60, "S": 60 * 60},
    "M": {"Y": 1 / (365 * 24 * 60), "W": 1 / (7 * 24 * 60), "D": 1 / (24 * 60), "H": 1 / 60, "S": 60},
    "S": {"Y": 1 / (365 * 24 * 60 * 60), "W": 1 / (7 * 24 * 60 * 60), "D": 1 / (24 * 60 * 60), "H": 1 / (60 * 60),
          "M": 1 / 60}
}


def convert_time(value, from_, to):
    if from_.upper() == to.upper():
        return value

    factor = CONVERSION_FACTORS[from_.upper()][to.upper()]

    return round(value * factor, 2)
