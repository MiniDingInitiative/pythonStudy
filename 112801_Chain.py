# -*- coding: utf-8 -*-
#!/usr/bin/env python
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__

Chain().status.user.timeline.list


class Student(object):
    def __init__(self, name):
        self.name = name
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an interger!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0~100!')
        self._score = score

    def __call__(self):
        print('My name is %s.' % self.name)
    def __getattr__(self, attr):
        if attr == 'name':
            print('Stdent name is %s.' % name)
        raise AttributeError('\'Student\' has no attribute \'%s\'' % attr)


s = Student('Steve')
s()
s = Student('Danny')
# s()
s.score = 66
print(s.score)
callable(Student('Hanmeimei'))
