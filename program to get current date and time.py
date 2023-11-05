Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> current_time = datetime.datetime.now()
>>> print("Time now at greenwich meridian is : ", current_time )
Time now at greenwich meridian is :  2023-11-05 16:16:03.916160
>>> 
>>> 
>>> import datetime
>>> current_time = datetime.datetime.now()
>>> print("The attributes of now() are : ")
The attributes of now() are : 
>>> print("Year: ", current_time.year)
Year:  2023
>>> print("Month: ", current_time.month)
Month:  11
>>> print("Day: ", current_time.day)
Day:  5
>>> print("Hour: ", current_time.hour)
Hour:  16
>>> print("Minute: ", current_time.minute)
Minute:  17
>>> print("Second: ", current_time.second)
Second:  3
>>> print("Microsecond: ", current_time.microsecond)
Microsecond:  153404
