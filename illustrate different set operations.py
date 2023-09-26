Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> E = {0,2,4,6,8};
>>> N = {1,2,3,4,5};
>>> print("Union of E and N is", E | N)
Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}
>>> print("intersection of E and N is", E & N)
intersection of E and N is {2, 4}
>>> print("difference of E and N is", E - N)
difference of E and N is {0, 8, 6}
>>> print("symmetric difference of E and N is", E ^ N)
symmetric difference of E and N is {0, 1, 3, 5, 6, 8}
