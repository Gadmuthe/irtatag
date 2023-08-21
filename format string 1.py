Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = 'values'
y = 100
print('''string formatting lets you insert {} into strings. 
they can even be numbers, like {}.''' .format(x,y))
string formatting lets you insert values into strings. 
they can even be numbers, like 100.


var_a = 'A'
var_b = 'B'
print('{a}, {b}'.format(b = var_b, a = var_a))
A, B


var_a = 'G'
var_b = 'A'
print('{1}, {0}' .format(var_a, var_b))
A, G
print('{0}, {1}' .format(var_a, var_b))
G, A


print('{}, {}, {}, {}, {}.....' .format(1, 2, 3, 4, 5))
1, 2, 3, 4, 5.....


print('{0}{1}{0}' .format('abra', 'cad'))
abracadabra


var_a = 15
var_b = 70
print(f'{var_a} + {var_b}')
15 + 70
print(f'{var_a + var_b}')
85
print(f'var_a = {var_a} \nvar_b = {var_b}')
var_a = 15 
var_b = 70


num = 1000.987123
>>> f'{num:.2f}'
'1000.99'
>>> 
>>> 
>>> num = 1000.987123
>>> print(f'{num:.3e}')
1.001e+03
>>> decimal = 0.2497856
>>> print(f'{decimal:.4%}')
24.9786%
>>> 
>>> 
>>> my_string = 'happy birthday'
>>> print(my_string.count('y'))
2
>>> print(my_string.count('y', 2, 7))
1
>>> 
>>> 
>>> my_string = 'happy birthday'
>>> my_string.find('birth')
6
>>> 
>>> 
>>> separator_string = ''
>>> iterable_of_strings = ['happy', 'birthday', 'to', 'you']
>>> separator_string.join(iterable_of_strings)
'happybirthdaytoyou'
>>> 
>>> 
>>> my_string = 'do you know the muffin man?'
>>> my_string.split()
['do', 'you', 'know', 'the', 'muffin', 'man?']
>>> 
>>> 
>>> import re
>>> my_string = 'three sad tigers swallowed wheat in a wheat field'
>>> re.search('[bms]ad', my_string)
<re.Match object; span=(6, 9), match='sad'>
