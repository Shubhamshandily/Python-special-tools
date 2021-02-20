from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x=[1,2,3]
y=[4,5,1]

x2=[1,4,6]
y2=[4,5,2]

plt.plot(x,y,'r',label='Line one',linewidth=5)
plt.plot(x2,y2,'b',label='Line two',linewidth=5)

plt.title('INFO')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()

plt.grid(True,color='k')

plt.show()
