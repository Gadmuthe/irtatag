Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
my_tuple = ()
print(my_tuple)
()
my_tuple = (1,2,3)
print(my_tuple)
(1, 2, 3)
my_tuple = (1, "hello", 3.4)
print(my_tuple)
(1, 'hello', 3.4)
my_tuple = ("mouse", [8,4,6], (1,2,3))
print(my_tuple)
('mouse', [8, 4, 6], (1, 2, 3))


var1 = ("hello")
print(type(var1))
<class 'str'>
var2 = ("hello",)
print(type(var2))
<class 'tuple'>
var3 = "hello",
print(type(var3))
<class 'tuple'>


letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters)
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(letters[0])
p
print(letters[5])
a
print(letters[-1])
z
>>> print(letters[-3])
m
>>> print(letters[1:4])
('r', 'o', 'g')
>>> print(letters[:-7])
('p', 'r')
>>> print(letters[7:])
('i', 'z')
>>> print(letters[:])
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
>>> ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
>>> 
>>> 
>>> my_tuple = ('a', 'p', 'p', 'l', 'e',)
>>> print(my_tuple.count('p'))
2
>>> print(my_tuple.index('l'))
3
>>> 
>>> 
>>> languages = ('python', 'swift', 'c++')
>>> for language in languages:
...     print(language)
...     print(language)
... 
python
python
swift
swift
c++
c++
>>> 
>>> 
>>> languages = ('python', 'swift', 'c++')
>>> print('c' in languages)
False
>>> print('python' in languages)
True
