Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}
>>> print("The dictionary before performing remove is: ", test_dict)
The dictionary before performing remove is:  {'Arushi': 22, 'Mani': 21, 'Haritha': 21}
>>> del test_dict['Mani']
>>> print("The dictionary after remove is: ", test_dict)
The dictionary after remove is:  {'Arushi': 22, 'Haritha': 21}
>>> 
>>> 
>>> 
>>> test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
>>> print(test_dict)
{'Arushi': 22, 'Anuradha': 21, 'Mani': 21, 'Haritha': 21}
>>> test_dict.clear()
>>> print("Length", len(test_dict))
Length 0
>>> print(test_dict)
{}
>>> 
>>> 
>>> 
>>> test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
>>> print(test_dict)
{'Arushi': 22, 'Anuradha': 21, 'Mani': 21, 'Haritha': 21}
>>> del test_dict
>>> try:
...     print(test_dict)
... except:
...     print('Deleted!')
... 
...     
Deleted!
>>> 
>>> 
>>> 
>>> test_dict = {"Arushi": 22, "Anurahda": 21, "Mani": 21, "Haritha": 21}
>>> print(test_dict)
{'Arushi': 22, 'Anurahda': 21, 'Mani': 21, 'Haritha': 21}
y = {}
for key, value in test_dict.items():
    if key != 'Arushi':
        y[key] = value

        
print(y)
{'Anurahda': 21, 'Mani': 21, 'Haritha': 21}
