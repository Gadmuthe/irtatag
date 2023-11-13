Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pickle
>>> try:
...     geeky_file = open('GFG.txt', 'r')
...     dictionary_list = pickle.load(geeky_file)
...     for d in dictionary_list:
...         print(d)
...     geeky_file.close()
... except:
...     print("Something unexpected occured!")
... 
...     
Something unexpected occured!
