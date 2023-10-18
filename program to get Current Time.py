Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> now_method = datetime.now()
>>> currentTime = now_method.strftime("%H:%M:%S")
>>> print("Current Time =", currentTime)
Current Time = 23:53:23
>>> 
>>> 
>>> from datetime import datetime
>>> time = datetime.now().time()
>>> print("Current Time =", time)
Current Time = 23:55:08.205756
>>> 
>>> 
>>> import time
>>> Time = time.localtime()
>>> currentTime = time.strftime("%H:%M:%S", Time)
>>> print(currentTime)
23:55:42
