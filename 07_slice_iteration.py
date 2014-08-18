#Slice&Iteration

#Slice
# (list/tuple/string)[start_index=0:end_index:step=1]
print range(13)[2:-3:2]

#Iteration
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
	print k
for v in d.itervalues():
	print v
for k,v in d.iteritems():
	print k,'=',v
#from collections import Iterable
#isinstance('abc', Iterable) #str是否可迭代
for i, value in enumerate(['A', 'B', 'C']):
	print i, value
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y