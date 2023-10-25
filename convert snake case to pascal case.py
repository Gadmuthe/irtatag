Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string
>>> test_str = 'geeksforgeeks_is_best'
>>> print("The original string is: "+ test_str)
The original string is: geeksforgeeks_is_best
>>> print("The original string is: " + test_str)
The original string is: geeksforgeeks_is_best
>>> res = string.capwords(test_str.replace("_", " ")).replace(" ", "")
>>> print("The string after changing case: "+ str(res))
The string after changing case: GeeksforgeeksIsBest
>>> 
>>> 
>>> string = 'geeksforgeeks_is_best'
>>> words = string.split('_')
>>> capitalized_words = [word.title() for word in words]
>>> result = ''.join(capitalized_words)
>>> print(result)
GeeksforgeeksIsBest
