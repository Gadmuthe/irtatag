Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> punctuations = '''!()-[]{};:'\,<>./?@#$%^&*_~`'''
>>> my_str = "hello!!!, he said ---and went."
>>> no_punct = ""
>>> for char in my_str:
...     if char not in punctuations:
...         no_punct = no_punct + char
...         print(no_punct)
... 
...         
h
he
hel
hell
hello
hello 
hello h
hello he
hello he 
hello he s
hello he sa
hello he sai
hello he said
hello he said 
hello he said a
hello he said an
hello he said and
hello he said and 
hello he said and w
hello he said and we
hello he said and wen
hello he said and went
