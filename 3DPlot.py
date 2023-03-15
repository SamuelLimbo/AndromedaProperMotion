import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = open('VelRad.txt', 'r')

radius = []
PAang  = []    
iang   = []
vel    = []

for line in f:
    columns = line.split()
    try:
        radius.append(float(columns[0])/60)
        PAang.append(float(columns[4])*np.pi/180)
        iang.append(float(columns[7])*np.pi/180)
        vel.append(float(columns[8]))
    except:
        continue
        
t = np.linspace(0, 2*np.pi, 100)
x, y, z = [], [], []

for i in range(len(radius)):
    if radius[i] < 2.3:
        x.append(radius[i]*np.cos(t))
        y.append(radius[i]*np.cos(iang[i])*np.sin(t))
        z.append(-radius[i]*np.sin(iang[i])*np.sin(t))
    else:
        break
        
ax = plt.figure().add_subplot(projection='3d')
for i in range(len(x)):
    ax.plot(x[i], y[i], z[i])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
