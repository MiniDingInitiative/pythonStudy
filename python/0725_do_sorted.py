# -*- coding: utf-8 -*-
#!/usr/bin/env python
print(sorted([-1, 44, -99, 36, 99, 1], key= abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit', 'zoo'], key = str.lower, reverse = True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
print(sorted(L, key = by_name))

def by_score(t):
    return t[1]
print(sorted(L, key = by_score, reverse = True))
