#Bar Graph
print("\nBar Graph")
from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Bar Label A")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Bar Label B",color='g')
plt.legend()
plt.xlabel('Bar Number')
plt.ylabel('Bar Height')

plt.title('Bar Graph')
plt.show()

#Histogram
print("\nHistogram\n")
import matplotlib.pyplot as plt

population_age=[22,55,62,45,21,22,34,42,42,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_age,bins,histtype='bar',rwidth=.8,label="Population Age")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.legend()
plt.show()

#Scatter
print("Scatter Plot")
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='skitscat',color='b',s=25,marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot\n')
plt.legend()
plt.show()

#Stack plot
print("\nStack Plot")
import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([],[],color='m',label='Sleeping',linewidth=5)
plt.plot([],[],color='c',label='Eating',linewidth=5)
plt.plot([],[],color='r',label='Working',linewidth=5)
plt.plot([],[],color='b',label='Playinging',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Stck/Area Plot')
plt.legend()
plt.show()

#PieChart
print("\nPieChart\n")
import matplotlib.pyplot as plt

slices=[7,2,2,13]
activities=['Sleeping','Eating','Working','Playing']
cols=['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('Pie Chart')
plt.show()

#Multiple PLot
print("\nMultiple Plot\n")
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)* np.cos(2*np.pi*t)

t1= np.arange(0.0,5.0,0.1)
t2= np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(t1,f(t1), 'bo',t2,f(t2))

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()
