from literal import ConvertTime, DateDiff
from datetime import datetime
from difference import date_diff, convert_time

if __name__ == "__main__":
    t = ConvertTime('2021-05-31 23:16:55.321568', 'd')
    p = ConvertTime(datetime.now(), 'd')
    i = ConvertTime('2021-05-31 23:16:55+00:00', 'd')
    d = ConvertTime('2021-05-31', time_format='d')
    e = DateDiff('2021-05-31', '2021-04-31', 'd')
    print(t.slug_date_time)
    print(i.slug_date_time)
    print(d.slug_date)
    print(e.date_diff)
    print(date_diff('2021-08-31', '2021-05-30', 'D'))
    print(convert_time(1, "y", 'h'))







