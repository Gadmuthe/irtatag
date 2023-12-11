Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def rev_sentence(sentence):
...     words = sentence.split(' ')
...     reverse_sentence = ' '.join(reversed(words))
...     return reverse_sentence
... 
>>> if __name__ == "__main__":
...     input = 'quiz practice code'
...     print(rev_sentence(input))
... 
...     
code practice quiz
>>> 
>>> 
>>> 
>>> import re
>>> def rev_sentence(sentence):
...     words = re.findall('\w+', sentence)
...     reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))
...     return reverse_sentence
... 
>>> if __name__ == "__main__":
...     input = 'quiz practice code'
...     print(rev_sentence(input))
... 
...     
code practice quiz
