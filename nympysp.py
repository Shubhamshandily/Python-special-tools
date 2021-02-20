#NUMPY SPECIAL FUNCTION
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,3*np.pi,0.1)


y= np.sin(x)
#z=np.tan(x)
a=np.cos(x)

plt.plot(x,y)
#plt.plot(x,z)
plt.plot(x,a)

plt.show()

#Exponrtial and Log Function
print("\nExponrtial and Log Function\n")
ar=np.array([(1,2,3),(4,5,6)])
print(np.exp(ar))
print(np.log(ar))
print(np.log10(ar))
