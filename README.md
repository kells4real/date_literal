# date_literal
A python package to convert date or datetime formats to literal days, hours, minutes or seconds for comparison or whatever. 
For example, you can convert DateTime objects to know just how much of a difference there is between them, or you just want 
to get human read-able format of DateTime or Date objects.

## Installation
pip install date_time_literal

## Usage
#### IMPORTANT
DateTime or Date objects must be in the default 'Y-M-D Hr:Min:Sec' and 'Y-M-D' formats respectively.

### CONVERT DATE TIME
from date_time_literal import ConvertTime
from django.utils import timezone
time = timezone.now()

##### Converts Date Time Literal
convert_time = ConvertTime(time).slug_date_time

##### Converts Date Literal
convert_time = ConvertTime(time).slug_date
This returns the date or date-time in seconds. You can add an optional parameter to specify what you want.

Note: You can use the slug_date class function on a DateTime object if you wish to use only the date part of the DateTime object, 
but cannot use the slug_date_time class function on a Date object, only on DateTime objects.

#### Specific conversion to days
convert_time = ConvertTime(time, 'd').slug_date_time
convert_time = ConvertTime(time, 'd').slug_date

#### Specific conversion to hours
convert_time = ConvertTime(time, 'h').slug_date_time

#### Specific conversion to minutes
convert_time = ConvertTime(time, 'm').slug_date_time

The default conversion if none is specified is to seconds

### CHECK DATE-TIME OR DATE DIFFERENCE BETWEEN TWO DATE-TIME OR DATE LITERALS
from date_time_literal import date_time_diff, date_diff

date_l = date_diff(date1, date2, 'd')
date_time_l = date_time_diff(date_time1, date_time2, 'd')

This will return the difference in value between date_l and date_time_l in days. You can use the 
corresponding string literal to get for minutes, hours and seconds which is the default value.

