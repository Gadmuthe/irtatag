Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def checkDivisibility(n, digit):
...     return(digit != 0 and n % digit == 0)
... 
>>> def allDigitsDivide( n) :
...     temp = n
...     while(temp > 0):
...         digit = temp % 10
...         if ((checkDivisibility(n, digit)) == False) :
...             return False
...         temp = temp // 10
...     return True
... 
>>> n = 128
>>> if(allDigitsDivide(n)) :
...     print("Yes")
... else:
...     print("No")
... 
...     
Yes
