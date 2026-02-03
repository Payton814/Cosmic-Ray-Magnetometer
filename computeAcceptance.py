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

R = 25362 ## Radius of the planet in km
          ## Uranus: R = 25362 km



a = []
b = []
b2max = 0
b2min = 10000000000000000000000000

Nthrow = 10000000

## Enter the monte carlo loop
## Currently done horribly with just a giant for loop
for i in range(Nthrow):
    #print(sc.lat, sc.long)
    #sc.lat = 0
    #sc.long = 0

    ## With the spacecraft initialized we can throw a cosmic ray
    ## throwCR only needs the spacecraft object. It then uses the 
    ## spacecraft latitude and longitude, as well as field of view (currently just a whole half sphere)
    ## and samples a point on the planet surface and then gets the direction of the CR
    ## NOTE: Thinking about changing the output of throwCR to be a cosmic ray object. But I need to create
    ## a cosmic ray class first. Sigh, later me problems. Or maybe I can find an undergrad to do this.
    CR_r0, CR_dir, CR_lat, CR_long = throwCR(sc, R + sc.altitude)

    #print(CR_r0, CR_dir)

    b2 = CR_r0[0]**2 + CR_r0[1]**2 + CR_r0[2]**2 - (CR_r0[0]*CR_dir[0] + CR_r0[1]*CR_dir[1] + CR_r0[2]*CR_dir[2])**2
    if (b2 > b2max):
        b2max = b2
    if (b2 < b2min):
        b2min = b2
    if (b2 < (R + 100)**2 and b2 > (R - 100)**2):
        event = 1
    else:
        event = 0

    if (event == 1):
        event = projectCRCone(sc, CR_r0, CR_dir, R + sc.altitude)

    if (event == 1):
        a.append(CR_lat)
        b.append(CR_long)
    rates = np.append(rates, [event])

    updateSC(sc)

plt.scatter(a, b, marker = 'o')
plt.show()

print(np.sqrt(b2max) - R, np.sqrt(b2min))

#Acceptance = 4*np.pi*(R+sc.altitude)**2*(2*np.pi*(np.cos((1.62-0.01)*np.pi/180) - np.cos((1.62+0.01)*np.pi/180)))*np.sum(rates)/Nthrow
Acceptance = 4*np.pi**2*(R + sc.altitude)**2*(np.sum(rates)/Nthrow)
print(np.sum(rates)/Nthrow, Acceptance)
print(2*np.pi*R*(2*100)*4*np.pi*(1.62*np.pi/180)*(0.01*np.pi/180))
#print(2*np.pi*69000*70*4*np.pi*(0.4*np.pi/180)*(0.02*np.pi/180))