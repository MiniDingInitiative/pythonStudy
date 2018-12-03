# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 装饰器 在代码运行期动态增加的方式，称之为装饰器
def log(func):
    def wrapper(* args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2018-07-26')
f = now
print(f())
print(now.__name__)
print(f.__name__)
print(now())
