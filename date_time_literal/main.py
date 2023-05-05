from literal import ConvertTime, DateDiff
from datetime import datetime
from difference import date_diff, convert_time, date_time_diff

if __name__ == "__main__":
    t = ConvertTime('2021-05-31 23:16:55.321568', 'd')
    p = ConvertTime(datetime.now(), 'd')
    i = ConvertTime('2021-05-31 23:16:55+00:00', 'd')
    d = ConvertTime('2021-05-31', time_format='d')
    e = DateDiff('2021-05-31 23:16:55+00:00', '2021-04-30 23:16:55+00:00', 'h')
    print(t.slug_date_time)
    print(i.slug_date_time)
    print(d.slug_date)
    print(e.date_diff)
    print(date_time_diff('2021-04-30 21:56:50+00:00', '2021-04-30 10:58:55+00:00', 'm'))
    print(convert_time(1, "w", 'y'))









