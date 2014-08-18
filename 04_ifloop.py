#If&Loop
# -*- coding: utf-8 -*-

#if...elif...else
age = int(raw_input('input your age:'))
if age >= 50:
    print u'老马'
elif age >= 20:
    print u'骏马'
else:
    print u'小丁丁'
#for
sum = 0
for x in range(101):
    sum += x
print sum
#while
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print sum