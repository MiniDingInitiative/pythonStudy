#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0~100!')
        self._score = score

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, birth):
        self._birth = birth
    @property
    def age(self):
        return 2018 - self._birth
s = Student()
s.score = 60
s.score = 99

s.birth = 25
print(s.age)
