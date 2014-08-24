#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()



# xxx.py = module
# xxx/__init__.py , xxx = package
# xxx/yyy.py , xxx.yyy

# from xxxModule import xFunction|xClass
# import xxx as x
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

# __xxx__ : 特殊变量
# _xxx __xxx :private

# Module SearchPath
import sys
sys.path

sys.path.append('/xxx/yyy')
# PYTHONPATH

# 安装第三方模块
# python ez_setup.py
# easy_install PIL

# __future__ py2.x ==> py3.x
from __future__ import division
print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3