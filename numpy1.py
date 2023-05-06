
from  numpy import *
 
a =arange(15)


b = add.reduce(a)

print(a)
print(b)

from  numpy import *
 
a =arange(2,8)


b = multiply.reduce(a)

print(a)
print(b)


from  numpy import *
 
a =arange(2,8)


b = multiply.accumulate(a)

print(a)
print(b)
from  numpy import *
 
a =arange(12)
b = len(a)

c = a.reshape(3,4)
d = len(c)

print(a)
print(b)
print(c)
print(d)
from  numpy import *
 
a =arange(12)
b = a.shape

c = a.reshape(3,4)
d = c.shape

print(a)
print(b)
print(c)
print(d)



from  numpy import *
 
a =array(['a','d','g','h','j'])
b = a.dtype

c = arange(12)
d = c.reshape(3,4)
e = d.dtype

print(a)
print(b)
print(c)
print(d)
print(e)

a = matrix('{} {} ; {} {}'.format(1,2,3,4))
b = matrix('{} {} ;{} {}; {} {}'.format(1,2,3,4,5,6))

print(a)
print(b)




from  numpy import *

a =arange(9)
b = a.reshape(3,3)
c = linalg.det(b)
d = linalg.eig(b)


print(a)
print(b)
print(c)
print(d)

a =arange(20) 

c = a[3]
d = a[3:15]
e = a[3:9:2]
f = a[-1]
g = a[-9]

print(a)
print(c)
print(d)
print(e)
print(f)
print(g)

from  numpy import *

a =arange(36).reshape(6,6)

c = a[3]
d = a[3:9]
e = a[3:9:2]
f = a[-1]
g = a[-3]

print(a)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
print('-------------------------')
print(f)
print('-------------------------')
print(g)

from  numpy import *

a =arange(36).reshape(6,6)

c = a[3,1]
d = a[3,:]
e = a[:,2]
f = a[:,1:3]
g = a[1:2,:]

print(a)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
print('-------------------------')
print(f)
print('-------------------------')
print(g)
