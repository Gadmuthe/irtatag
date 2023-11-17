Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_str = "ScoobyDooby"
>>> print("The original string is: "+ test_str)
The original string is: ScoobyDooby
>>> all_freq = {}
>>> for i in test_str:
...     if i in all_freq:
...         all_freq[i] += 1
...     else:
...         all_freq[i] = 1
... 
...         
>>> res = max(all_freq, key = all_freq.get)
>>> print("The maximum of all characters in ScoobyDooby is: "+ str(res))
The maximum of all characters in ScoobyDooby is: o
>>> 
>>> 
>>> 
>>> test_str = "ScoobyDooby"
>>> res = max(test_str, key=lambda x: test_str.count(x))
>>> print(res)
o
