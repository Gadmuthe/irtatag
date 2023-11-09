Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_tuple1 = (4,5)
>>> test_tuple2 = (7,8)
>>> print("The original tuple 1: " + str(test_tuple1))
The original tuple 1: (4, 5)
>>> print("The original tuple 2: " + str(test_tuple2))
The original tuple 2: (7, 8)
>>> res = [(a,b) for a in test_tuple1 for b in test_tuple2 ]
>>> res = res+ [(a,b) for a in test_tuple2 for b in test_tuple1]
>>> print("The filtered tuple: " + str(res))
The filtered tuple: [(4, 7), (4, 8), (5, 7), (5, 8), (7, 4), (7, 5), (8, 4), (8, 5)]
