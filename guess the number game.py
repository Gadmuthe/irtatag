Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> secret_number = random.randint(1, 100)
>>> guess = None
>>> while guess != secret_number:
...     guess = int(input("guess the number (1-100): "))
...     if guess < secret_number:
...         print("Too  low! Try again. ")
...     elif guess > secret_number:
...         print("Too high! Try again.")
...     else:
...         print("Congratulations! you guessed the number. ")
... 
...         
guess the number (1-100): 10
Too  low! Try again. 
guess the number (1-100): 100
Too high! Try again.
guess the number (1-100): 15
Too  low! Try again. 
guess the number (1-100): 2509
Too high! Try again.
guess the number (1-100): 77
Too high! Try again.
guess the number (1-100): 70
Too high! Try again.
guess the number (1-100): 50
Too  low! Try again. 
guess the number (1-100): 60
Too  low! Try again. 
guess the number (1-100): 65
Too high! Try again.
guess the number (1-100): 63
Too high! Try again.
guess the number (1-100): 62
Too high! Try again.
guess the number (1-100): 61
Congratulations! you guessed the number. 
