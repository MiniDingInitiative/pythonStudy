# -*- coding: utf-8 -*-
#!/usr/bin/env python

class Animal(object):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

#大类：
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#各种动物
class Dog(Mammal, RunnableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass

class Parrot(Bird, FlyableMixIn):
    pass

class Ostrich(Bird, RunnableMixIn):
    pass

# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass
husky = Dog()
husky.run()

class MyTCPServer(TCPServer, ForkingMixIn):
    pass

class MyUDPServer(UDPServer, ThreadingMixin):
    pass


class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A, B):
    pass

class C2(A, B):
    pass

class D(C1, C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d = D()
    d.foo()
    d.bar()
