Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
cities = ['paris', 'lagos', 'mumbai']
countries = ['france', 'nigeria', 'india']
places = zip(cities, countries)
print(places)
<zip object at 0x102e91d80>
print(list(places))
[('paris', 'france'), ('lagos', 'nigeria'), ('mumbai', 'india')]
>>> 
>>> 
>>> scientists = [('nikola', 'tesla'), ('charles', 'darwin'), ('marie', 'curie')]
>>> given_names, surnames = zip(*scientists)
>>> print(given_names)
('nikola', 'charles', 'marie')
>>> print(surnames)
('tesla', 'darwin', 'curie')
>>> 
>>> 
>>> letters = ['a', 'b', 'c']
>>> for index, letter in enumerate(letters):
...     print(index, letter)
... 
...     
0 a
1 b
2 c
>>> 
>>> letters = ['a', 'b', 'c']
>>> for index, letter in enumerate(letters, 2):
...     print(index, letter)
... 
...     
2 a
3 b
4 c
>>> 
>>> 
>>> numbers = [1, 2, 3, 4, 5]
>>> new_list = [x + 10 for x in numbers]
>>> print(new_list)
[11, 12, 13, 14, 15]
>>> 
>>> 
>>> words = ['emotan', 'amina', 'ibeno', 'sankwala']
>>> new_list =  [(word[0], word[-1]) for word in words if len(word) > 5]
>>> print(new_list)
[('e', 'n'), ('s', 'a')]
