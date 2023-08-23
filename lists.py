Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = ['now', 'we', 'are', 'cooking', 'with', 7, 'ingredients']
>>> print(x[3])
cooking
>>> x[1:3]
['we', 'are']
>>> x[:2]
['now', 'we']
>>> x[2:]
['are', 'cooking', 'with', 7, 'ingredients']
>>> type(x)
<class 'list'>
>>> 
>>> 
>>> fruits = ['pineapple', 'banana', 'apple', 'melon']
>>> fruits.append('kiwi')
>>> print(fruits)
['pineapple', 'banana', 'apple', 'melon', 'kiwi']
>>> fruits.insert(0, 'mango')
>>> print(fruits)
['mango', 'pineapple', 'banana', 'apple', 'melon', 'kiwi']
>>> fruits.remove('banana')
>>> print(fruits)
['mango', 'pineapple', 'apple', 'melon', 'kiwi']
>>> fruits.pop(2)
'apple'
