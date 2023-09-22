Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
rows = int(input("enter number of rows: "))
enter number of rows: 7
for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print(" ", end="")
    for j in range(i, 2*i-1):
        print("*", end="")
    for j in range(1, i-1):
        print("*", end="")
    print()

    
***********
 *********
  *******
   *****
    ***
     *


rows = int(input("enter the number of rows: "))
enter the number of rows: 7
coef = 1
>>> for i in range(1, rows+1):
...     for space in range(1, rows-i+1):
...         print(" ", end="")
...     for j in range(0, i):
...         if j==0 or i==0:
...             coef = 1
...         else:
...             coef = coef * (i-j)//j
...         print(coef, end = "")
...     print()
... 
...     
      1
     11
    121
   1331
  14641
 15101051
1615201561
>>> 
>>> 
>>> #floyds triangle
>>> rows = int(input("enter number of rows: "))
enter number of rows: 7
>>> number = 1
>>> for i in range(1, rows+1):
...     for j in range(1, i+1):
...         print(number, end=" ")
...         number += 1
...     print()
... 
...     
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 
