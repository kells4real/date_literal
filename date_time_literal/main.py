from classes import ConvertTime, DateDiff
from functions import *
from datetime import datetime

if __name__ == "__main__":
    t = ConvertTime('2021-05-31 23:16:55.321568', time_format='d')
    p = ConvertTime(datetime.now(), time_format='d')
    i = ConvertTime('2021-05-31 23:16:55+00:00', time_format='d')
    d = ConvertTime('2021-05-31', time_format='d')
    e = DateDiff('2021-05-31', '2021-03-31', time_format='d')
    # print(t.slug_date_time)
    # print(i.slug_date_time)
    # print(d.slug_date)
    print(e.date_diff)






