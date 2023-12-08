Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from itertools import product
>>> test_dict = {'month' : [1,2,3],
...              'name' : ['Jan', 'Feb', 'March']}
>>> 
>>> print("The original dictionary is : " + str(test_dict))
The original dictionary is : {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
>>> res = dict(zip(test_dict['month'], test_dict['name']))
>>> print("Flattened dictionary: " + str(res))
Flattened dictionary: {1: 'Jan', 2: 'Feb', 3: 'March'}
>>> 
>>> 
>>> 
>>> test_dict = {'month' : [1,2,3],
...              'name' : ['Jan', 'Feb', 'March']}
>>> print("The original dictionary is: " +str(test_dict))
The original dictionary is: {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
>>> x = list(test_dict.values())
>>> a=x[0]
>>> b=x[1]
>>> d=dict()
>>> for i in range(0,len(a)):
...     d[a[i]]=b[i]
... 
...     
>>> print("Flattened dictionary: " + str(d))
Flattened dictionary: {1: 'Jan', 2: 'Feb', 3: 'March'}
