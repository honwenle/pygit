#!/usr/bin/env python
# -*- coding: utf-8 -*-

### 类、实例
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def get_score(self):
    	return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

mage = Student(u'马亚民', 59)
mage.print_score()
print mage.get_grade()
print mage.get_score()
mage.set_score(99)
print mage.get_score()
print mage._Student__name

### 继承、多态
class Animal(object):
    def run(self):
        print 'Animal is running...'
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'
class Cat(Animal):
    def run(self):
        print 'Cat is running...'
mym = Dog() # c是Dog类型
print isinstance(mym, Animal)
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())

### 获取对象信息
