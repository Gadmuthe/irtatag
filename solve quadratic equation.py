Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cmath
>>> a = 1
>>> b = 5
>>> c = 6
>>> d = (b**2) - (4*a*c)
>>> sol1 = (-b-cmath.sqrt(d))/(2*a)
>>> sol2 = (-b+cmath.sqrt(d))/(2*a)
>>> print('the solution are {0} and {1}'.format(sol1, sol2))
the solution are (-3+0j) and (-2+0j)
