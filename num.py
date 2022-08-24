import numpy as np
import matplotlib.pyplot as plt

plt.figure
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
plt.plot(x , y, 'r',x , y+6, 'b' )
plt.ylabel('No of people')
plt.xlabel('No of hours')
plt.title('Y Vs X')

name = ['A','B','C']
vales = [10,20,50]

plt.bar(name,vales)


plt.show()