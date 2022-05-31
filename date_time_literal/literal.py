
class ConvertTime:
    def __init__(self, time, time_format='s'):
        self.time = time
        self.time_: str = time_format

    @property
    def slug_date_time(self):
        slug_time = str(self.time)
        first = slug_time.split("-")
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
        if self.time_ == 'm':
            get_days_mins = (hrs * 60) + mins
            get_years_mins = (years + months + days) * 24 * 60
            return get_years_mins + get_days_mins
        elif self.time_ == 'h':
            get_days_mins = (hrs * 60) + mins
            get_years_mins = (years + months + days) * 24 * 60
            return round((get_years_mins + get_days_mins) / 60, 2)
        elif self.time_ == 'd':
            get_years_days = years + months + days
            return get_years_days
        else:
            get_days_secs = (hrs * 60 * 60) + (mins * 60) + secs_int
            get_years_secs = (years + months + days) * 24 * 60 * 60
            return get_years_secs + get_days_secs

    @property
    def slug_date(self):
        slug_time: str = str(self.time)
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
        if self.time_ == 'm':
            get_mins = (years + months + days) * 24 * 60
            return get_mins
        elif self.time_ == 'h':
            get_hrs = round(((years + months + days) * 24 * 60) / 60, 2)
            return get_hrs
        elif self.time_ == 'd':
            get_days = years + months + days
            return get_days
        else:
            get_secs = (years + months + days) * 24 * 60 * 60
            return get_secs


class DateDiff:
    def __init__(self, time1, time2, time_format='s'):
        self.time1 = time1
        self.time2 = time2
        self.time_: str = time_format

    @property
    def date_time_diff(self):
        # time 1
        slug_time1 = str(self.time1)
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
        slug_time2 = str(self.time2)
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

        if self.time_ == 'm' or self.time_ == 'M':
            get_days_mins = (hrs * 60) + mins
            get_years_mins = (years + months + days) * 24 * 60
            get_days_mins2 = (hrs2 * 60) + mins2
            get_years_mins2 = (years2 + months2 + days2) * 24 * 60
            return (get_years_mins + get_days_mins) - (get_years_mins2 + get_days_mins2)
        elif self.time_ == 'h' or self.time_ == 'H':
            get_days_mins = (hrs * 60) + mins
            get_years_mins = (years + months + days) * 24 * 60
            get_days_mins2 = (hrs2 * 60) + mins2
            get_years_mins2 = (years2 + months2 + days2) * 24 * 60
            return round((get_years_mins + get_days_mins) - (get_years_mins2 + get_days_mins2) / 60, 2)
        elif self.time_ == 'd' or self.time_ == 'D':
            get_days = years + months + days
            get_days2 = years2 + months2 + days2
            return get_days - get_days2
        else:
            get_days_secs = (hrs * 60 * 60) + (mins * 60) + secs_int
            get_years_secs = (years + months + days) * 24 * 60 * 60
            get_days_secs2 = (hrs2 * 60 * 60) + (mins2 * 60) + secs_int2
            get_years_secs2 = (years2 + months2 + days2) * 24 * 60 * 60
            return (get_years_secs + get_days_secs) - (get_days_secs2 + get_years_secs2)

    @property
    def date_diff(self):
        # time 1
        slug_time = str(self.time1)
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
        slug_time = str(self.time2)
        first2 = slug_time.split("-")
        second2 = first2[0:2]
        third2 = first2[2]
        i2 = second2[0]
        j2 = second2[1]
        k2 = third2.split(" ")[0]
        year_in_days2 = int(i2) * 365
        years2 = int(year_in_days)
        months2 = int(j2) * 30
        days2 = int(k2)

        if self.time_ == 'm' or self.time_ == 'm':
            get_mins = (years + months + days) * 24 * 60
            get_mins2 = (years2 + months2 + days2) * 24 * 60
            return get_mins - get_mins2
        elif self.time_ == 'h' or self.time_ == 'H':
            get_mins = (years + months + days) * 24 * 60
            get_mins2 = (years2 + months2 + days2) * 24 * 60
            return round((get_mins - get_mins2) / 60, 2)
        elif self.time_ == 'd' or self.time_ == 'D':
            get_days = years + months + days
            get_days2 = years2 + months2 + days2
            return get_days - get_days2
        else:
            get_secs = (years + months + days) * 24 * 60 * 60
            get_secs2 = (years2 + months2 + days2) * 24 * 60 * 60
            return get_secs - get_secs2

