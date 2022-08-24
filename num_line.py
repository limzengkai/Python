import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,235, 267, 278,288,298,306,314,321,328,334])
y = np.array([0,10000,20000,30000,40000,50000,600000,70000,80000,90000,100000])


plt.subplot(1, 2, 1)
plt.plot(x,y,ms='10',mec='r',mfc='y',ls=':',c='#4618ED',lw='3')
plt.title("Coivid-19 in Malaysia")
plt.xlabel("Days")
plt.ylabel("Number of cases")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y,"--yo",ms='15',lw='10')
plt.title("Y2 vs X2")
plt.xlabel("X2 is me")
plt.ylabel("y2 is me")

plt.show()