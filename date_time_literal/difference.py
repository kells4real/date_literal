
def date_time_diff(time1, time2, time_='s'):
    # time 1
    slug_time1 = str(time1)
    first = slug_time1.split("-")
    second = first[0:2]
    third = first[2]
    fourth = third.split(" ")[1].split(":")
    i = second[0]
    j = second[1]
    k = third.split(" ")[0]
    hrs = int(fourth[0])
    mins = int(fourth[1])
    secs = fourth[2].split(".")[0]
    if '+' in secs:
        secs = secs.split('+')[0]
    secs_int = int(secs)
    year_in_days = int(i) * 365
    years = int(year_in_days)
    months = int(j) * 30
    days = int(k)

    # time2
    slug_time2 = str(time2)
    first2 = slug_time2.split("-")
    second2 = first2[0:2]
    third2 = first2[2]
    fourth2 = third2.split(" ")[1].split(":")
    i2 = second2[0]
    j2 = second2[1]
    k2 = third2.split(" ")[0]
    hrs2 = int(fourth2[0])
    mins2 = int(fourth2[1])
    secs2 = fourth2[2].split(".")[0]
    if '+' in secs2:
        secs2 = secs2.split('+')[0]
    secs_int2 = int(secs2)
    year_in_days2 = int(i2) * 365
    years2 = int(year_in_days2)
    months2 = int(j2) * 30
    days2 = int(k2)

    if time_ == 'm' or time_ == 'M':
        get_days_mins = (hrs * 60) + mins
        get_years_mins = (years + months + days) * 24 * 60
        get_days_mins2 = (hrs2 * 60) + mins2
        get_years_mins2 = (years2 + months2 + days2) * 24 * 60
        return (get_years_mins + get_days_mins) - (get_years_mins2 + get_days_mins2)
    elif time_ == 'h' or time_ == 'H':
        get_hrs = (years + months + days) * 24
        get_hrs2 = (years2 + months2 + days2) * 24
        return get_hrs - get_hrs2
    elif time_ == 'd' or time_ == 'D':
        get_days = years + months + days
        get_days2 = years2 + months2 + days2
        return get_days - get_days2
    else:
        get_days_secs = (hrs * 60 * 60) + (mins * 60) + secs_int
        get_years_secs = (years + months + days) * 24 * 60 * 60
        get_days_secs2 = (hrs2 * 60 * 60) + (mins2 * 60) + secs_int2
        get_years_secs2 = (years2 + months2 + days2) * 24 * 60 * 60
        return (get_years_secs + get_days_secs) - (get_days_secs2 + get_years_secs2)


def date_diff(time1, time2, time_='s'):
    # time 1
    slug_time = str(time1)
    first = slug_time.split("-")
    second = first[0:2]
    third = first[2]
    i = second[0]
    j = second[1]
    k = third.split(" ")[0]
    year_in_days = int(i) * 365
    years = int(year_in_days)
    months = int(j) * 30
    days = int(k)

    # time 2
    slug_time = str(time2)
    first2 = slug_time.split("-")
    second2 = first2[0:2]
    third2 = first2[2]
    i2 = second2[0]
    j2 = second2[1]
    k2 = third2.split(" ")[0]
    year_in_days2 = int(i2) * 365
    years2 = int(year_in_days2)
    months2 = int(j2) * 30
    days2 = int(k2)

    if time_ == 'm' or time_ == 'm':
        get_mins = (years + months + days) * 24 * 60
        get_mins2 = (years2 + months2 + days2) * 24 * 60
        return get_mins - get_mins2
    elif time_ == 'h' or time_ == 'H':
        get_hrs = (years + months + days) * 24
        get_hrs2 = (years2 + months2 + days2) * 24
        return get_hrs - get_hrs2
    elif time_ == 'd' or time_ == 'D':
        get_days = years + months + days
        get_days2 = years2 + months2 + days2
        return get_days - get_days2
    else:
        get_secs = (years + months + days) * 24 * 60 * 60
        get_secs2 = (years2 + months2 + days2) * 24 * 60 * 60
        return get_secs - get_secs2


def convert_time(value, from_, to):
    if from_ == "Y" or from_ == "y":
        if to == "D" or to == "d":
            v = value * 365
            return v
        elif to == "H" or to == 'h':
            v = value * 365 * 24
            return v
        elif to == "M" or to == "m":
            v = value * 365 * 24 * 60
            return v
        else:
            v = value * 365 * 24 * 60 * 60
            return v

    elif from_ == "D" or from_ == "d":
        if to == "Y" or to == "y":
            v = value / 365
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        elif to == "H" or to == 'h':
            v = value * 24
            return v
        elif to == "M" or to == "m":
            v = value * 24 * 60
            return v
        else:
            v = value * 24 * 60 * 60
            return v

    elif from_ == "H" or from_ == "h":
        if to == "D" or to == "d":
            v = value / 24
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        elif to == "Y" or to == 'y':
            v = (value / 24) / 365
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        elif to == "M" or to == "m":
            v = value * 60
            return v
        else:
            v = value * 60 * 60
            return v

    elif from_ == "M" or from_ == "m":
        if to == "D" or to == "d":
            v = (value / 60) / 24
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        elif to == "Y" or to == 'y':
            v = ((value / 60) / 24) / 365
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        elif to == "H" or to == "h":
            v = value / 60
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        else:
            v = value * 60
            return v

    elif from_ == "S" or from_ == "s":
        if to == "D" or to == "d":
            v = ((value / 60) / 60) / 24
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        elif to == "Y" or to == 'y':
            v = (((value / 60) / 60) / 24) / 365
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        elif to == "H" or to == "h":
            v = (value / 60) / 60
            if str(v).split('.')[1] != '0':
                return round(v, 5)
            else:
                return int(v)
        else:
            v = value * 60
            return v
