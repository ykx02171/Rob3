import matplotlib.pyplot as plt
import numpy as np
import math
import mpl_toolkits.mplot3d.axes3d


fig = plt.figure()
ax1 = plt.axes()

x = np.array([5,8])
y = np.array([12,-6])
z = np.array([0,0])
ax1.scatter(x,y,c='r')

# B1
plt.show()
