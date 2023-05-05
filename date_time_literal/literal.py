
class ConvertTime:
    def __init__(self, time, time_format='s'):
        self.time = time
        self.time_: str = time_format

    @property
    def convert_time(self):
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
    def convert(self):
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
        self.time_ = time_format

    def _get_year_month_day(self, slug_time):
        first = slug_time.split("-")
        second = first[0:2]
        third = first[2].split(" ")[0]
        year_in_days = int(second[0]) * 365
        years = year_in_days // 365
        months = int(second[1]) * 30
        days = int(third)
        return years, months, days

    def _get_hours_minutes_seconds(self, slug_time):
        fourth = slug_time.split(" ")[1].split(":")
        hrs = int(fourth[0])
        mins = int(fourth[1])
        secs = fourth[2].split(".")[0]
        if '+' in secs:
            secs = secs.split('+')[0]
        secs_int = int(secs)
        return hrs, mins, secs_int

    @property
    def date_time_diff(self):
        # time 1
        years, months, days = self._get_year_month_day(str(self.time1))
        hrs, mins, secs_int = self._get_hours_minutes_seconds(str(self.time1))

        # time 2
        years2, months2, days2 = self._get_year_month_day(str(self.time2))
        hrs2, mins2, secs_int2 = self._get_hours_minutes_seconds(str(self.time2))

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
            return get_years_secs + get_days_secs


