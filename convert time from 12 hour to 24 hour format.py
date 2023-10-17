Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def convert24(str1):
...     if str1[-2:] == "AM" and str1[:2] == "12":
...         return "00" + str1[2:-2]
...     elif str1[-2:] == "AM":
...         return str1[:-2]
...     elif str1[-2:] == "PM" and str1[:2] == "12":
...         return str1[:-2]
...     else:
...         return str(int(str1[:2]) + 12) + str1[2:8]
...     print(convert24("08:05:45 PM"))
... 
...     
>>> 
>>> 
>>> from datetime import datetime
>>> def convert24(time):
...     t = datetime.strptime(time, '%I:%M:%S %p')
...     return t.strftime('%H:%M:%S')
...     print(convert24('11:21:30 PM'))
...     print(convert24('12:12:20 AM'))
... 
...     
>>> 
>>> import re
>>> def convert_to_24hour(time_str):
...     hour, minute, second, am_pm = re.findall('\d+|\w+', time_str)
...     hour = int(hour)
...     if am_pm == 'PM' and hour != 12:
...         hour += 12
...     elif am_pm == 'AM' and hour == 12:
...         hour = 0
...     return f'{hour:02d}: {minute}: {second}'
...     print(convert_to_24hour('11:21:30 PM'))
...     print(convert_to_24hour('12:12:20 AM'))
... 
...     
