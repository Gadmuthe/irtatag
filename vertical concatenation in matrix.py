Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_list = [["Scooby", "good"], ["is", "for"], ["Best"]]
>>> print("The original list: " + str(test_list))
The original list: [['Scooby', 'good'], ['is', 'for'], ['Best']]
>>> res = []
>>> N = 0
>>> while N != len(test_list):
...     temp = ' '
...     for idx in test_list:
...         try: temp = temp + idx[N]
...         except IndexError: pass
...     res.append(temp)
...     N = N + 1
... 
...     
>>> res = [ele for ele in res if res]
>>> print("List after column Concatenation: " + str(res))
List after column Concatenation: [' ScoobyisBest', ' goodfor', ' ']
>>> 
>>> 
>>> 
>>> from itertools import zip_longest
>>> test_list = [["Scooby", "good"], ["is", "for"], ["Best"]]
>>> print("The original list: " + str(test_list))
The original list: [['Scooby', 'good'], ['is', 'for'], ['Best']]
>>> res = ["".join(ele) for ele in zip_longest(*test_list, fillvalue = "")]
>>> print("List after column Concatenation: " + str(res))
List after column Concatenation: ['ScoobyisBest', 'goodfor']
