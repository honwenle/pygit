#!/usr/bin/env python
# -*- coding: utf-8 -*-

### 动态绑定 & __slots__
class Student(object):
    pass
s = Student()
s.name = 'Mage' #动态添加属性
print s.name
def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s,Student) #动态为实例绑定方法
s.set_age(13)
print s.age
s2 = Student() # s2.set_age(14)调用失败
def set_score(self,score):
    self.score = score
Student.set_score = MethodType(set_score,None,Student) #动态为类绑定方法

class Ma(object):
    __slots__ = ('name','age') #tuple定义允许的属性名
m = Ma()
m.name = 'Mage'
m.age = '12'
# m.score = 78 #赋值失败
class LaoMa(Ma):
    pass
lm = LaoMa()
lm.score = 87

### @property
class Xia(object):
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,rgb):
        if rgb < 770000:
            raise ValueError('color must be red, such as ruby!')
        self._color = rgb
    # birth can read also can write ,  age is ReadOnly,bcoz No setter
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2014 - self._birth
xx = Xia()
xx.color = 880000
print xx.color
# xx.color = 660000 #会报自定义的错喔

### Mixin
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print('running...')
class Flyable(object):
    def fly(self):
        print('flying...')
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
class Parrot(Bird,Flyable):
    pass
class Ostrich(Bird,Runnable):
    pass

#这课完了之后，先复习前面、加注释和重点、再学习调试