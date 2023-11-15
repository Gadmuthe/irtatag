Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random as rn
>>> dict = {}
>>> x,y,z = 10,20,30
>>> dict[x,y,z] = x+y-z;
>>> x,y,z = 5,2,4
>>> dict[x,y,z] = x+y-z;
>>> print(dict)
{(10, 20, 30): 0, (5, 2, 4): 3}
>>> 
>>> 
>>> 
>>> places = {("19.07'53.2", "72.54'51.0"): "Mumbai", \
...           ("28.33'34.1", "77.06'16.6"): "Delhi"}
>>> print(places)
{("19.07'53.2", "72.54'51.0"): 'Mumbai', ("28.33'34.1", "77.06'16.6"): 'Delhi'}
>>> print('\n')


>>> lat = []
>>> long = []
>>> plc = []
>>> for i in places:
...     lat.append(i[0])
...     long.append(i[1])
...     plc.append(places[i[0], i[1]])
... 
...     
>>> print(lat)
["19.07'53.2", "28.33'34.1"]
>>> print(long)
["72.54'51.0", "77.06'16.6"]
>>> print(plc)
['Mumbai', 'Delhi']
