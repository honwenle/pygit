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
# m.score = 78 赋值失败
class LaoMa(Ma):
	pass
lm = LaoMa()
lm.score = 87

#这课完了之后，先复习前面、加注释和重点、再学习调试