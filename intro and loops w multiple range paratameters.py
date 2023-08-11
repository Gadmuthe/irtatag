Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
for x in range(5):
    print(x)

    
0
1
2
3
4
>>> 
>>> 
>>> product = 1
>>> for i in range(1,10):
...     product = product * i
...     print(product)
... 
...     
1
2
6
24
120
720
5040
40320
362880
>>> 
>>> 
>>> def to_celsius(x):
...     return(x-32) * 5/9
... 
>>> for x in range(0,101,10):
...     print(x, to_celsius(x))
... 
...     
0 -17.77777777777778
10 -12.222222222222221
20 -6.666666666666667
30 -1.1111111111111112
40 4.444444444444445
50 10.0
60 15.555555555555555
70 21.11111111111111
80 26.666666666666668
90 32.22222222222222
100 37.77777777777778
