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
# type() 基本类型、函数、类
type(xxx)
import types
type('abc')==types.StringType
type(int)==type(str)==types.TypeType
# isinstance() 对象是否属于类
isinstance(u'a', unicode)
isinstance(u'a', (str, unicode))
isinstance(u'a', basestring)
# dir() 对象的所有属性和方法
print dir('ABC')
len('ABC')
'ABC'.__len__()
'ABC'.lower()

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
hasattr(obj, 'x') # 有属性'x'吗？
obj.x
hasattr(obj, 'y') # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
hasattr(obj, 'y') # 有属性'y'吗？
getattr(obj, 'y') # 获取属性'y'
obj.y # 获取属性'y'
getattr(obj, 'z') # 获取属性'z'
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
hasattr(obj, 'power') # 有属性'power'吗？
getattr(obj, 'power') # 获取属性'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn # fn指向obj.power
fn() # 调用fn()与调用obj.power()是一样的