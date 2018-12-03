#!/usr/bin/env python3
# -*- coding: utf-8 -*-

std1 = {'name' : 'Jenny', 'score' : 98}
std2 = {'name' : 'Danny', 'score' : 80}

def print_score(std):
    print('%s: %s' %(std['name'], std['score']))

print_score(std1)


class Student(object):
    def __init__(self, name, score, gender):
        self.name = name
        self.__score = score
        self.__gender = gender
    def print_score(self):
        print('%s: %s' %(self.name, self.score))
    def set_score(self, score):
        self.__score = score
    def get_score(self):
        return self.__score

    def set_gender(self, gender):
        if gender == 'male':
            self.__gender = gender
        elif gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender')
    def get_gender(self):
        return self.__gender

# bart = Student('Bart Simpson', 59, 'malell')
# print(bart.get_score())
# lisa = Student('Lisa Simpson', 88, 'malell')
#
# bart.__score = 'New Score'
# print(bart.__score)

bart = Student('Bart', 99, 'male')
if bart.get_gender() != 'male':
    print('faile!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('faile!')
    else:
        print('success!')
