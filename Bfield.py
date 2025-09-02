import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


## I here by define the coordinate system such that z goes through the north pole.
## Positive x goes through longitude = 0

longitude = np.linspace(0, 2*np.pi, 360) ## on a map these are the vertical lines. So changing line moves east west
latitude = np.linspace(0, np.pi, 180) ## On a map this is the horizontal lines. So to move lines you move north south

def Bfield(latitude, longitude):
    B_r = 0
    B_theta = 0
    B_phi = latitude/(2*np.pi)
    B = B_phi
    return B

X = np.zeros((len(latitude), len(longitude)))
for i in range(len(latitude)):
    for ii in range(len(longitude)):
        X[i][ii] = Bfield(latitude[i], longitude[ii])

xlabel = np.linspace(0, 2*np.pi, 10)
ylabel = np.linspace(0, np.pi, 5)

df = pd.DataFrame(X)

df.to_csv('linear_LUT.csv')

plt.imshow(X, origin = 'lower')
plt.xticks(xlabel)
plt.colorbar()
plt.show()


