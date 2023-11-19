import matplotlib.pyplot as plt
import numpy as np
import math
import mpl_toolkits.mplot3d.axes3d

fig = plt.figure()
ax1 = plt.axes()

x = np.array([5, 8])
y = np.array([12, -6])
z = np.array([0, 0])
ax1.scatter(x, y, c='r')

# B1
# plt.show()

a_trans = np.array([5, 12, 0])
b_trans = np.array([8, -6, 0])

b = b_trans.reshape(b_trans.shape[0], 1)
a = a_trans.reshape(a_trans.shape[0], 1)

a_norm = np.linalg.norm(a)
b_norm = np.linalg.norm(b)

uv_b = b/b_norm
# print(b_trans)
# print(a)
b_cross = np.dot(b, b.T)
b_cross_norm = np.dot(uv_b,uv_b.T)
print('b_cross', b_cross)

projection_b_a = np.dot(b_cross, a)
print('projection_b_a', projection_b_a)

projection_b_norm_a = np.dot(b_cross_norm,a)
print('projection_b_norm_a', projection_b_norm_a)
ax1.scatter(-256, 192, c='b', marker='o')
ax1.scatter(-2.56, 1.92, c='b', marker='o')
# plt.show()

b_skew = np.array([[0, 0, -6],
                   [0, 0, -8],
                   [6, 8, 0]])

b_sun = np.dot(-b_skew, b_skew)
b_sun_norm = np.dot(-b_skew/b_norm,b_skew/b_norm)
print('b_sun', b_sun)

rejection_b_a = np.dot(b_sun, a)
print('rejection_b_a', rejection_b_a)
rejection_b_norm_a = np.dot(b_sun_norm,a)
print('rejection_b_norm_a',rejection_b_norm_a)

ax1.scatter(756, 1008, c='b', marker='o')
ax1.scatter(7.56, 10.08, c='b', marker='o')
#plt.show()

orthogonal_b_a = np.dot(b_cross,a)
print('orthogonal_b_a',orthogonal_b_a)

orthogonal_b_a_norm = np.dot(b_cross_norm,a)
print('orthogonal_b_a_norm',orthogonal_b_a_norm)