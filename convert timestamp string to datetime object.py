Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> timestamp_string = "2023-07-21 15:30:45"
>>> format_string = "%Y-%m-%d %H:%M:%S"
>>> datetime_object = datetime.strptime(timestamp_string, format_string)
>>> print(datetime_object)
2023-07-21 15:30:45
>>> 
>>> 
>>> from datetime import datetime
>>> timestamp = 1545730073
>>> dt_obj = datetime.fromtimestamp(1140825600)
>>> print("date_time:", dt_obj)
date_time: 2006-02-25 05:30:00
>>> print("type of dt:", type(dt_obj))
type of dt: <class 'datetime.datetime'>
