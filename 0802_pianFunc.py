# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
import functools
print(int('4',base = 8))
print(int('16',base = 16))

def int2(x, base = 2):
    return int(x, base)

print(int2('10000000'))

int3 = functools.partial(int, base = 2)
print(int3('1000001'))

max2 = functools.partial(max, 10)
print(max2(1, 9, 0, 8))

def serach_word_in_filename(path, str):
    for x in os.listdir(path):
        if os.path.isfile(x) and str in x:
            print(os.path.join(os.path.abspath(path),x))
        if os.path.isdir(x):
            serach_word_in_filename(x, str)
try:
    serach_word_in_filename(sys.argv[1], sys.argv[2])
except:
    print('error')
finally:
    print('end')

# class partial:
#     def __new__(cls, func, *args, **kwargs):
#         if not callable(func):
#             raise TypeError('the first argument must be callable')
#         self = super().__new__(cls)
#         self.func = func
#         self.args = args
#         self.kwargs = kwargs
#         return self
#     def __call__(self, *args, **kwargs):
#         newkeywords = self.kwargs.copy()
#         newkeywords.update(kwargs)
#         return self.func(*self.args, *args, **newkeywords)
# def add(x, y):
#     return x + y
# inc = partial(add, y = 1)
# print(inc(41))

def my_partial(func, args, **kwargs):
    def newfunc(as, kw):
        for k in kw.keys():
            kwargs[k] = kw[k]
        return func(*(args+as),ks)
    return newfunc
