Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
team = [
    ('marta', 20, 'center'),
    ('ana', 22, 'point guard'),
    ('gabi', 22, 'shooting guard'),
    ('luz', 21, 'power forward'),
    ('lorena', 19, 'small forward'),
    ('sandra', 19, 'center'),
    ('mari', 18, 'point guard'),
    ('esme', 18, 'shooting guard'),
    ('lin', 18, 'power forward'),
    ('sol', 19, 'small forward'),
    ]
new_team = {}
for name, age, position in team:
    if position in new_team:
        new_team[position].append((name, age))
    else:
        new_team[position] = [(name, age)]
        new_team

        
{'center': [('marta', 20)]}
{'center': [('marta', 20)], 'point guard': [('ana', 22)]}
{'center': [('marta', 20)], 'point guard': [('ana', 22)], 'shooting guard': [('gabi', 22)]}
{'center': [('marta', 20)], 'point guard': [('ana', 22)], 'shooting guard': [('gabi', 22)], 'power forward': [('luz', 21)]}
{'center': [('marta', 20)], 'point guard': [('ana', 22)], 'shooting guard': [('gabi', 22)], 'power forward': [('luz', 21)], 'small forward': [('lorena', 19)]}
>>> 
>>> new_team['point guard']
[('ana', 22), ('mari', 18)]
>>> 
>>> for x in new_team:
...     print(x)
... 
...     
center
point guard
shooting guard
power forward
small forward
>>> 
>>> new_team.keys()
dict_keys(['center', 'point guard', 'shooting guard', 'power forward', 'small forward'])
>>> 
>>> new_team.values()
dict_values([[('marta', 20), ('sandra', 19)], [('ana', 22), ('mari', 18)], [('gabi', 22), ('esme', 18)], [('luz', 21), ('lin', 18)], [('lorena', 19), ('sol', 19)]])
>>> 
>>> for a, b in new_team.items():
...     print(a, b)
... 
...     
center [('marta', 20), ('sandra', 19)]
point guard [('ana', 22), ('mari', 18)]
shooting guard [('gabi', 22), ('esme', 18)]
power forward [('luz', 21), ('lin', 18)]
small forward [('lorena', 19), ('sol', 19)]
