# date_literal
A package/module for converting date or date-time formats to literal days, hours, minutes, or seconds for comparison or whatever. 
For example, you can convert DateTime objects to know just how much of a difference there is between them, or you just want 
to get the human-readable format of DateTime or Date objects.

## Installation
> pip install date_time_literal

## Usage
#### IMPORTANT
DateTime or Date objects must be in the default 'Y-M-D Hr:Min:Sec' and 'Y-M-D' formats respectively.

##### Converts Date Time Literal
```python
from django.utils import timezone
time = timezone.now()
from date_time_literal import ConvertTime
convert_time = ConvertTime(time).slug_date_time
```
##### Converts Date Literal
convert_time = ConvertTime(time).slug_date
This returns the date or date-time in seconds. You can add an optional parameter to specify what you want.

Note: You can use the slug_date class function on a DateTime object if you wish to use only the date part of the DateTime object, 
but cannot use the slug_date_time class function on a Date object, only on DateTime objects.

#### Specific conversion to days

```python
from django.utils import timezone
from datetime import datetime
from date_time_literal import ConvertTime

time2 = datetime.now()
time = timezone.now()

convert_time = ConvertTime(time, 'd').slug_date_time
convert_time2 = ConvertTime(time2, 'd').slug_date
```

#### Specific conversion to hours

```python
from date_time_literal import ConvertTime
from datetime import datetime
time = datetime.now()
convert_time = ConvertTime(time, 'd').slug_date_time # Converts the DateTime object to days
convert_time1 = ConvertTime(time, 'h').slug_date_time # Converts the DateTime object to hours
convert_time2 = ConvertTime(time, 'm').slug_date_time # Converts the DateTime object to minutes

# The default conversion if none is specified is to seconds
```

### CHECK DATE-TIME OR DATE DIFFERENCE BETWEEN TWO DATE-TIME OR DATE LITERALS

```python
from date_time_literal import ConvertTime
from datetime import datetime
from django.utils import timezone
time = datetime.now()
convert_time = ConvertTime(time, 'h').slug_date_time
from date_time_literal import date_time_diff, date_diff
convert_time2 = ConvertTime(time, 'm').slug_date_time
date1 = '2021-05-31'
date2 = '2021-03-21'
date_time1 = timezone.now()
date_time2 = '2021-03-21 23:16:45.735963'
date_l = date_diff(date1, date2, 'd')
date_time_l = date_time_diff(date_time1, date_time2, 'd')

# date_time_l will return the difference in value between date_time1 and date_time2 in days. You can use the 
# corresponding string literal to get for minutes, hours and seconds which is the default value.
# date_time_diff returns the difference in two dateTimes to the second. This should be used when you need to get 
# date time difference to the last second

```

## Convert between time and dates
You can also use the convert_time function to convert between times

```python
from date_time_literal import convert_time

# Converts between years, days, hours, minutes, and seconds
print(convert_time(365, 'd', 'y')) # Converts 365 days to years
print(convert_time(5, 'y', 'd')) # Converts 5 years to days
print(convert_time(5, 'y', 'h')) # Converts 5 years to hours
print(convert_time(5, 'd', 's')) # Converts 5 days to seconds
# etc
```

### Some Basic use cases
To get a rather comprehensive idea of how the package works, copy the code below and run it. The convert_time function
was updated to be more efficient and now allows for week conversion as well in version 1.0.8

```python
from date_time_literal import ConvertTime, DateDiff, date_diff, convert_time
from datetime import datetime

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
print(convert_time(365, 'd', 'y'))

```
