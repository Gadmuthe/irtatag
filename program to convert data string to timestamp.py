Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> import datetime
>>> string ="20/01/2020"
>>> element = datetime.datetime.strptime(string, "%d/%m/%Y")
>>> tuple = element.timetuple()
>>> timestamp = time.mktime(tuple)
>>> print(timestamp)
1579458600.0
>>> 
>>> 
>>> 
>>> import time
>>> import datetime
>>> string = "20/01/2020"
>>> element = datetime.datetime.strptime(string, "%d/%m/%Y")
>>> timestamp = datetime.datetime.timestamp(element)
>>> print(timestamp)
1579458600.0
