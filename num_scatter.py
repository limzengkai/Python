import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,6])
y = np.array([5,6,7,8,7])
colors = np.array(["red","yellow","black","blue","grey"])
plt.scatter(x, y,c=colors)
plt.colorbar()
plt.show()