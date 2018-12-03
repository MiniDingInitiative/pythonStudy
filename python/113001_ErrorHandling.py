#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import logging
# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     # bar('0')
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
    #     print('Error:', e)
    # finally:
    #     print('finally')
# try:
#     print('try...')
#     r = 10 / int(True)
#     print('retsult:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error')
# finally:
# #     print('finally...')
# main()
# print('END')

# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
# foo('0')



# from functools import reduce
#
# def str2num(s):
#     return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()

#错误调试
#断言
# import logging
# logging.basicConfig(level = logging.INFO)
# def foo(s):
#     n = int(s)
#     # assert n != 0, 'n is zero'
#     logging.info('n = %d' % n)
#     return 10 / n
# def main():
#     foo('0')
# main()
# print(logging.info())

import pdb
s = '0'
n = int(s)
pdb.set_trace
print(10 / n)
