Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> import calendar
>>> def day_occur_time(year):
...     days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday" ]
...     L = [52 for i in range(7)]
...     pos = -1
...     day = datetime.datetime(year, month = 1, day = 1).strftime("%A")
...     for i in range(7):
...         if day == days[i]:
...             pos = i
...     if calendar.isleap(year):
...         L[pos] += 1
...         L[(pos+1)% 7] += 1
...     else:
...         L[pos] += 1
...     for i in range(7):
...         print(days[i], L[i])
... 
...         
>>> year = 2019
>>> day_occur_time(year)
Monday 52
Tuesday 53
Wednesday 52
Thrusday 52
Friday 52
Saturday 52
Sunday 52
