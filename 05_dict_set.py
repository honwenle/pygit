#dict&set

#dict
jj = {'mage':3,'ucss':4,'hui':4}
print jj['mage'],'cm'
jj['noclip'] = 13
jj['mage'] = 3.3
print jj['mage'],'cm',jj['noclip'],'cm'
print 'jx' in jj
print jj.get('jx', 'jx no JJ')
jj.pop('ucss')
print jj
#set
s1 = set([2,3,4])
s1.add(1)
s1.remove(4)
s2 = set([1,3,5])
print s1 & s2
print s1 | s2