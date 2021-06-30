
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
    year_in_days = float(i) * 365.25
    years = int(year_in_days)
    months = int(float(j) * 30.5)
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
    year_in_days2 = float(i2) * 365.25
    years2 = int(year_in_days2)
    months2 = int(float(j2) * 30.5)
    days2 = int(k2)

    if time_ == 'm':
        get_days_mins = (hrs * 60) + mins
        get_years_mins = (years + months + days) * 24 * 60
        get_days_mins2 = (hrs2 * 60) + mins2
        get_years_mins2 = (years2 + months2 + days2) * 24 * 60
        return (get_years_mins + get_days_mins) - (get_years_mins2 + get_days_mins2)
    elif time_ == 'h':
        get_years_hrs = (years + months + days) * 24
        return get_years_hrs + hrs
    elif time_ == 'd':
        get_years_days = years + months + days
        return get_years_days
    else:
        get_days_secs = (hrs * 60 * 60) + (mins * 60) + secs_int
        get_years_secs = (years + months + days) * 24 * 60 * 60
        return get_years_secs + get_days_secs


def date_diff(time, time_='s'):
    slug_time = str(time)
    first = slug_time.split("-")
    second = first[0:2]
    third = first[2]
    i = second[0]
    j = second[1]
    k = third.split(" ")[0]
    year_in_days = float(i) * 365.25
    years = int(year_in_days)
    months = int(float(j) * 30.5)
    days = int(k)
    if time_ == 'm':
        get_mins = (years + months + days) * 24 * 60
        return get_mins
    elif time_ == 'h':
        get_hrs = (years + months + days) * 24
        return get_hrs
    elif time_ == 'd':
        get_days = years + months + days
        return get_days
    else:
        get_secs = (years + months + days) * 24 * 60 * 60
        return get_secs
