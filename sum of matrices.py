Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = [[12, 7, 3],
     [4,5,6],
     [7,8,9]]
y = [[5,8,1],
     [6,7,3],
     [4,5,9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
        for r in result:
            print(r)

            
[17, 0, 0]
[0, 0, 0]
[0, 0, 0]
[17, 15, 0]
[0, 0, 0]
[0, 0, 0]
[17, 15, 4]
[0, 0, 0]
[0, 0, 0]
[17, 15, 4]
[10, 0, 0]
[0, 0, 0]
[17, 15, 4]
[10, 12, 0]
[0, 0, 0]
[17, 15, 4]
[10, 12, 9]
[0, 0, 0]
[17, 15, 4]
[10, 12, 9]
[11, 0, 0]
[17, 15, 4]
[10, 12, 9]
[11, 13, 0]
[17, 15, 4]
[10, 12, 9]
[11, 13, 18]
>>> 
>>> 
>>> x = [[12,7,3],
...      [4,5,6],
...      [7,8,9]]
>>> y = [[5,8,1],
...      [6,7,3],
...      [4,5,9]]
>>> result = [[x[i][j] +y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
>>> for r in result:
...     print(r)
... 
...     
[17, 15, 4]
[10, 12, 9]
[11, 13, 18]
