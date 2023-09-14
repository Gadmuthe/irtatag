Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> vowels = 'aeiou'
>>> ip_str = 'hello, have you tired our tutorial section yet?'
>>> ip__str = ip_str.casefold()
>>> count = {}.fromkeys(vowels,0)
>>> for char in ip_str:
...     if char in count:
...         count[char] += 1
...         print(count)
... 
...         
{'a': 0, 'e': 1, 'i': 0, 'o': 0, 'u': 0}
{'a': 0, 'e': 1, 'i': 0, 'o': 1, 'u': 0}
{'a': 1, 'e': 1, 'i': 0, 'o': 1, 'u': 0}
{'a': 1, 'e': 2, 'i': 0, 'o': 1, 'u': 0}
{'a': 1, 'e': 2, 'i': 0, 'o': 2, 'u': 0}
{'a': 1, 'e': 2, 'i': 0, 'o': 2, 'u': 1}
{'a': 1, 'e': 2, 'i': 1, 'o': 2, 'u': 1}
{'a': 1, 'e': 3, 'i': 1, 'o': 2, 'u': 1}
{'a': 1, 'e': 3, 'i': 1, 'o': 3, 'u': 1}
{'a': 1, 'e': 3, 'i': 1, 'o': 3, 'u': 2}
{'a': 1, 'e': 3, 'i': 1, 'o': 3, 'u': 3}
{'a': 1, 'e': 3, 'i': 1, 'o': 4, 'u': 3}
{'a': 1, 'e': 3, 'i': 2, 'o': 4, 'u': 3}
{'a': 2, 'e': 3, 'i': 2, 'o': 4, 'u': 3}
{'a': 2, 'e': 4, 'i': 2, 'o': 4, 'u': 3}
{'a': 2, 'e': 4, 'i': 3, 'o': 4, 'u': 3}
{'a': 2, 'e': 4, 'i': 3, 'o': 5, 'u': 3}
{'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3}
