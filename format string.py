Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'manual'
>>> number = 3
>>> print('hello {}, your lucky number is {}' .format(name, number))
hello manual, your lucky number is 3
>>> 
>>> 
>>> price = 7.75
>>> with_tax = price * 1.07
>>> print('base price: ${} USD, \nwith tax: ${} USD.' .format(price, with_tax))
base price: $7.75 USD, 
with tax: $8.2925 USD.
>>> 
>>> 
>>> def to_celsius(x):
...     return(x-32) * 5/9
... 
>>> for x in range(0, 101, 10):
...     print("{:>3} F | {:>6.2F} C" .format(x, to_celsius(x)))
... 
...     
  0 F | -17.78 C
 10 F | -12.22 C
 20 F |  -6.67 C
 30 F |  -1.11 C
 40 F |   4.44 C
 50 F |  10.00 C
 60 F |  15.56 C
 70 F |  21.11 C
 80 F |  26.67 C
 90 F |  32.22 C
100 F |  37.78 C
