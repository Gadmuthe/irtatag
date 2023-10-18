Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime, timedelta
>>> presentday = datetime.now()
>>> yesterday = presentday - timedelta(1)
>>> tomorrow = presentday + timedelta(1)
>>> print("yesterday = ", yesterday.strftime('%d-%m-%y'))
yesterday =  18-10-23
>>> print("today = ", presentday.strftime('%d-%m-%y'))
today =  19-10-23
>>> print("tomorrow = ", tomorrow.strftime('%d-%m-%y'))
tomorrow =  20-10-23
