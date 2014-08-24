#!/usr/bin/env python
# -*- coding: utf-8 -*-

#匿名函数
lambda x: x * x

#函数作参数，返回函数
map(lambda x: x * x, [1, 2, 3, 4, 5])
def str2int(s):
    return reduce(lambda x,y: x*10+y, map(int, s))
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
#排序
sorted([36, 5, 12, 9, 21])