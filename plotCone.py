import numpy as np
import matplotlib.pyplot as plt
def f(x, y, z, x0, y0, z0, alpha, theta, phi):
    a = ((x - x0)*np.cos(phi) - (y - y0)*np.sin(phi))**2
    b = (((x - x0)*np.sin(phi) + (y - y0)*np.cos(phi))*np.cos(theta) - (z - z0)*np.sin(theta))**2
    c = (((x - x0)*np.sin(phi) + (y - y0)*np.cos(phi))*np.sin(theta) + (z - z0)*np.cos(theta))**2
    f = c*np.tan(alpha/2) - b - a
    return f
alpha = 30
theta = 45
phi = 45

x = []
y = []
z = []

for i in range(10000):
    
    w = -99
    while (w < 0):
        x0 = 10*np.random.random() - 5
        y0 = 10*np.random.random() - 5
        z0 = 10*np.random.random() - 5
        w = f(x0, y0, z0, 1, 1, 1, alpha*np.pi/180, theta*np.pi/180, phi*np.pi/180)
    x.append(x0)
    y.append(y0)
    z.append(z0)



fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(x, y, z, marker = 'o')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
plt.show()

