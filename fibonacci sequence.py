Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> nterms = int(input("how many terms? "))
how many terms? 7
>>> n1, n2 = 0, 1
>>> count = 0
>>> if nterms <= 0:
...     print("please enter a positive integer")
... elif nterms == 1:
...     print("fibonacci sequence upto",nterms,":")
...     print(n1)
... else:
...     print("fibonacci sequence:")
...     while count < nterms:
...         print(n1)
...         nth = n1 + n2
...         n1 = n2
...         n2 = nth
...         count +=1
... 
...         
fibonacci sequence:
0
1
1
2
3
5
8

#the two terms 0 and 1 are added to obtain the 3rd number then the next number
is added to the 4th number to obtain the 5th number and so on 
