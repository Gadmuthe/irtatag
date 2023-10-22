Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> def password(v) :
...     if v == "\n" or v == " ":
...         return "password cannoot be a newline or space!"
...     if 9 <= len(v) <= 20:
...         if re.search(r'(.)\1\1', v):
...             return "weak password: some character repeats three or more times in a row"
...         if re.search(r'(..)(.*?)\1', v):
...             return "weak password: same string pattern repetition"
...         else:
...             return "strong passsword!"
...     else:
...         return "password length must be 9-20 characters!"
... 
...     
>>> def main():
...     print(password("Qggf!@ghf3"))
...     print(password("Gggksforgeeks"))
...     print(password("aaabnillgu"))
...     print(password("Aasd!feasn"))
...     print(password("772*hd897"))
...     print(password(" "))
... 
...     
>>> if __name__ == '__main__':
...     main()
... 
...     
strong passsword!
weak password: same string pattern repetition
weak password: some character repeats three or more times in a row
weak password: same string pattern repetition
strong passsword!
password cannoot be a newline or space!
