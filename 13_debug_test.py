#!/usr/bin/env python
# -*- coding: utf-8 -*-

# try except finally
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'
# Exception都是继承的 https://docs.python.org/2/library/exceptions.html#exception-hierarchy

# 错误会一直往上抛
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
# main()

