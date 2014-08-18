#function
num = int(raw_input('input a number:'))
bijiao = cmp
print bijiao(abs(int('-13')),num)
#function-def
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print my_abs(-13)
def nop():
	pass
#function-def-return
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
(x,y) = move(100, 100, 60, math.pi / 6)
print x,y
#function-def-parameter
def my_pow(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print my_pow(3)
print my_pow(3,3)
#function-def-parameter-*
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
args = (1, 2, 3, 4)
kw = {'x': 99}
func(13,*args, **kw)