import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from throwCR import throwCR
from updateSC import updateSC
from spacecraft import spacecraft
from projectCRCone import projectCRCone
from scipy.interpolate import RegularGridInterpolator

import time

start_time = time.time()
## This is the main code for the Cosmic Ray Magnetometer monte carlo code
## Create the spacecraft object
sc = spacecraft()
rates = np.array([])
#df = pd.read_csv('./linear_LUT.csv', header = None)
#long = np.array(df.iloc[0, 1:])
#lat = np.array(df.iloc[1:, 0])
#B = np.array(df.iloc[1:, 1:])
#X, Y = np.meshgrid(long, lat)
#interp_func = RegularGridInterpolator((long, lat), B.T)
R = 25362 ## Radius of the planet in km
        ## Uranus: R = 25362 km
        ## Jupiter: R = 69000 km


Nthrow = int(sys.argv[1])


## Create an array of random spacecraft latitudes and longitudes
## Since we want the space craft location to be uniformly distributed on a sphere
## because of this, the latitude term is really uniform in cosine.
sc.lat = 180*np.acos((2*np.random.random(Nthrow) - 1))/np.pi
sc.long = 360*np.random.random(Nthrow)

sc.lat = np.zeros(Nthrow)
sc.long = np.zeros(Nthrow)


## NOTE: Thinking about changing the output of throwCR to be a cosmic ray object. But I need to create
## a cosmic ray class first. Sigh, later me problems. Or maybe I can find an undergrad to do this.

## throwCR will take in the imaginary sphere that cosmic rays are entering (Since were interacting in the
## atmosphere then we are some distance above the surface, so we need to start by throwing them into a sphere
## larger than the planet)
CR_r0, CR_dir, CR_lat, CR_long = throwCR(R + 1000, Nthrow)

print(CR_r0)
print(CR_dir)


b2 = CR_r0[:, 0]**2 + CR_r0[:, 1]**2 + CR_r0[:, 2]**2 - (CR_r0[:, 0]*CR_dir[:, 0] + CR_r0[:, 1]*CR_dir[:, 1] + CR_r0[:, 2]*CR_dir[:, 2])**2
b2max = np.max(b2)
b2min = np.min(b2)
mask = (b2 < (R + 100)**2) & (b2 > (R - 100)**2) 
event = projectCRCone(sc, CR_r0[mask], CR_dir[mask], R, mask)
rates = event.astype(int)
#print(np.sqrt(b2max) - R, np.sqrt(b2min))
#Acceptance = 4*np.pi*(R+sc.altitude)**2*(2*np.pi*(np.cos((1.62-0.01)*np.pi/180) - np.cos((1.62+0.01)*np.pi/180)))*np.sum(rates)/Nthrow
Acceptance = 4*np.pi**2*(R)**2*(np.sum(rates)/Nthrow)
print(np.sum(rates)/Nthrow, Acceptance)
print(2*np.pi*R*(2*100)*4*np.pi*(1.62*np.pi/180)*(0.02*np.pi/180))
#print(2*np.pi*69000*70*4*np.pi*(0.4*np.pi/180)*(0.02*np.pi/180))
end_time = time.time()
elapsed_time = end_time - start_time

print(str(int(sys.argv[2])), str(sys.argv[3]))

data = pd.DataFrame(data={"Elapsed Time (s)": [elapsed_time], "Number Thrown": [Nthrow], "Number Accepted": [np.sum(rates)], "Planet Radius (km)": [R], "Altitude (km)": [sc.altitude]})
data.to_csv(str(sys.argv[3]) + '/Run' + str(int(sys.argv[2])) + '.csv')

print("Elapsed Time: ", elapsed_time)
