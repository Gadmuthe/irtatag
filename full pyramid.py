Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> rows = int(input("enter number of rows: "))
enter number of rows: 7
>>> k = 0
>>> for i in range(1, rows+1):
...     for space in range(1, (rows-i)+1):
...         print(end = " ")
...     while k!=(2*i-1):
...         print("*", end="")
...         k+=1
...     k = 0
...     print()
... 
...     
      *
     ***
    *****
   *******
  *********
 ***********
*************
>>> 
>>> 
>>> rows = int(input("enter number of rows: "))
enter number of rows: 7
>>> k = 0
>>> count = 0
>>> count1 = 0
>>> for i in range(1, rows+1):
...     for space in range(1, (rows-1)+1):
...         print(" ", end="")
...         count+=1
...     while k!=((2*i)-1):
...         if count<=rows-1:
...             print(i+k, end=" ")
...             count+=1
...         else:
...             count+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    count1 = count = k = 0
    print()

    
      1 
      2 3 4 
      3 4 5 6 7 
      4 5 6 7 8 9 10 
      5 6 7 8 9 10 11 12 13 
      6 7 8 9 10 11 12 13 14 15 16 
      7 8 9 10 11 12 13 14 15 16 17 18 19 
