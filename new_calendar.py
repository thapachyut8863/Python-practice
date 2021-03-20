import calendar
import datetime
import time
print(calendar.weekheader(9))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 3))

print(calendar.monthcalendar(2020, 3))

print(calendar.calendar(2020))

print(calendar.calendar(2021))

print(calendar.calendar(2012))
print()
print(calendar.calendar(1995))
print()

print(calendar.monthcalendar(2020, 3))
print()

print(calendar.weekheader(9))
print()

print(calendar.calendar(2020))
print()

day_of_the_week = calendar.weekday(2020, 3, 29)
print(day_of_the_week)

is_leap = calendar.isleap(2000)
print(is_leap)

how_many_leap_day = calendar.leapdays(2000, 2040)
print(how_many_leap_day)


