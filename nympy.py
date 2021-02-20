import numpy as np

a= np.array([(1,2,3),(4,5,6)])
print(a)

#NUMPY Vs List space
print("NUMPY Vs List space")
import numpy as np
import time
import sys

s=range(1000)
print(sys.getsizeof(5)*len(s))

d=np.arange(1000)
print(d.size*d.itemsize)

#NUMPY Vs List speed
print("\nNUMPY Vs List speed\n")

size=100000

l1=range(size)
l2=range(size)

A1=np.arange(size)
A2=np.arange(size)

start =time.time()
result =[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

result=A1+A2
print((time.time()-start)*1000)

#NUMPY Operations
print("\nNumpy Operations\n")

b=np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print(b)
print(b.ndim)
print(b.itemsize)
print(b.dtype)

print(b.size)
print(b.shape)
#Reshape

#b=b.reshape(4,3)
print(b)

#slicing
print("\nslicing\n")
print(b[0,2])
print(b[0:,2])
print(b[0:2,3])

#LInespacing**************
print("\nLinespacing*****************\n")
a=np.linspace(1,5,10)
print(a)


print("\n MIN MAX SUM**\n")
print(b.max())
print(b.min())
print(b.sum())

print('\Axis\n')
v=np.array([(1,2,3),(4,5,6)])
print(v.sum(axis=0))
print(v.sum(axis=1))

print('\n Sqrt/Standard deviation\n')
print(np.sqrt(b))
print(np.std(b))

#NumPY Arithmetic Operstion
print("\n NumPY Arithmetic Operstion***********************\n")
j=np.array([(1,2,3,),(4,5,6)])
k=np.array([(1,2,3),(4,5,6)])
print(j+k)
print(j-k)
print(j*k)
print(j/k)

#Staking
print("\n Staking***************\n")
print(np.vstack((j,k)))
print(np.hstack((j,k)))

#Covering in single Row
print("\n Covering in single Row\n")
print(j.ravel())
