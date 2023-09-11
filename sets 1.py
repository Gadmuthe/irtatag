Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> example_a = [1, 2, 2.0, '2']
>>> set(example_a)
{1, 2, '2'}
>>> 
>>> example_b = ('apple', (1,2,2,2,3),2)
>>> set(example_b)
{'apple', 2, (1, 2, 2, 2, 3)}
>>> 
>>> set_1 = {'a','b','c'}
>>> set_2 = {'b', 'c', 'd'}
>>> print(set_1.difference(set_2))
{'a'}
>>> print(set_1 - set_2)
{'a'}
>>> 
>>> set_1 = {'a','b','c'}
>>> set_2 = {'b', 'c', 'd'}
>>> print(set_1.symmetric_difference(set_2))
{'a', 'd'}
>>> print(set_1 ^ set_2)
{'a', 'd'}
>>> 
>>> example_d = {'mother', 'hamster', 'father'}
>>> example_d.add('elderberries')
>>> example_d
{'mother', 'father', 'elderberries', 'hamster'}
>>> 
>>> example_e = [1.5, frozenset(['a', 'b', 'c']), 1.5]
>>> set(example_e)
{frozenset({'a', 'b', 'c'}), 1.5}
>>> 
>>> set_1 = {'a', 'b', 'c'}
>>> set_2 = {'b', 'c', 'd'}
>>> print(set_1.union(set_2))
{'c', 'd', 'a', 'b'}
>>> print(set_1 | set_2)
{'c', 'd', 'a', 'b'}

set_1 = {'a', 'b', 'c'}
set_2 = {'b', 'c', 'd'}
print(set_1.intersection(set_2))
{'b', 'c'}
print(set_1 & set_2)
{'b', 'c'}
