Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
num = 5
y = [1,2,3]
for num in y:
    print(num)
    print(num)

    
1
1
2
2
3
3

for i in range(3):
    print(i)

...     
0
1
2
>>> 
>>> for n in range(2,5):
...     print(n)
... 
...     
2
3
4
>>> 
>>> for even_num in range(2,11,2):
...     print(even_num)
... 
...     
2
4
6
8
10
>>> 
>>> students = [['igor', 'sokolov'], ['riko', 'miyazaki'], ['tuva', 'johnsen']]
>>> for student in students:
...     for name in student:
...         print(name)
...     print()
... 
...     
igor
sokolov

riko
miyazaki

tuva
johnsen

