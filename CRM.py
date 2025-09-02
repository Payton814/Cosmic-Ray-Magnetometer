import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from throwCR import throwCR
from updateSC import updateSC
from spacecraft import spacecraft
from projectCRCone import projectCRCone
from scipy.interpolate import RegularGridInterpolator

## This is the main code for the Cosmic Ray Magnetometer monte carlo code

## Create the spacecraft object
sc = spacecraft()

rates = np.array([])

df = pd.read_csv('./linear_LUT.csv', header = None)
long = np.array(df.iloc[0, 1:])
lat = np.array(df.iloc[1:, 0])
B = np.array(df.iloc[1:, 1:])

X, Y = np.meshgrid(long, lat)

interp_func = RegularGridInterpolator((long, lat), B.T)

a = []
b = []
## Enter the monte carlo loop
## Currently done horribly with just a giant for loop
for i in range(100000):
    #print(sc.lat, sc.long)

    ## With the spacecraft initialized we can throw a cosmic ray
    ## throwCR only needs the spacecraft object. It then uses the 
    ## spacecraft latitude and longitude, as well as field of view (currently just a whole half sphere)
    ## and samples a point on the planet surface and then gets the direction of the CR
    ## NOTE: Thinking about changing the output of throwCR to be a cosmic ray object. But I need to create
    ## a cosmic ray class first. Sigh, later me problems. Or maybe I can find an undergrad to do this.
    CR_r0, CR_dir, CR_lat, CR_long = throwCR(sc)

    event = projectCRCone(sc, CR_r0, CR_dir)
    if (event == 1):
        a.append(CR_lat)
        b.append(CR_long)
    rates = np.append(rates, [event])

    #updateSC(sc)

plt.scatter(a, b, marker = 'o')
plt.show()
print(np.sum(rates)/100000)