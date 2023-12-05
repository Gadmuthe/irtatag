Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import OrderedDict
>>> def checkOrder(input, pattern):
...     dict = OrderedDict.fromkeys(input)
...     ptrlen = 0
...     for key,value in dict.items():
...         if(key == pattern[ptrlen]):
...             ptrlen = ptrlen + 1
...         if(ptrlen == (len(pattern))):
...             return 'true'
...     return 'false'
... 
>>> if __name__ == "__main__":
...     input = 'engineers rock'
...     pattern = 'er'
...     print(checkOrder(input,pattern))
... 
...     
true
>>> 
>>> 
>>> 
>>> def check_order(string, pattern):
...     i, j = 0, 0
...     for char in string:
...         if char == pattern[j]:
...             j+= 1
...         if j == len(pattern):
...             return True
...         i+=1
...     return False
... 
>>> string = 'engineers rock'
>>> pattern = 'er'
>>> print(check_order(string, pattern))
True
