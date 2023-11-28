Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Fibonacci(n):
...     if n<= 0:
...         print("Incorrect input")
...     elif n == 1:
...         return 0
...     elif n == 2:
...         return 1
...     else:
...         return Fibonacci(n-1)+Fibonacci(n-2)
... 
...     
>>> print(Fibonacci(10))
34
>>> 
>>> 
>>> 
>>> FibArray = [0, 1]
>>> def fibonacci(n):
...     if n<0:
...         print("Incorrect input")
...     elif n<= len(FibArray):
...         return FibArray[n-1]
...     else:
...         temp_fib = fibonacci(n-1)+fibonacci(n-2)
...         FibArray.append(temp_fib)
...         return temp_fib
... 
...     
>>> print(fibonacci(9))
21
