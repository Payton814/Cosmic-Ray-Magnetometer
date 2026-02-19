import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from throwCR import throwCR
from updateSC import updateSC
from spacecraft import spacecraft
from projectCRCone import projectCRCone
from Bfield import Bfield_Earth_dipole
from Efield import Efield_simple
from helper_funcs import cartesian_to_spherical, spherical_to_cartesian, Fspherical_to_cartesian
from scipy.interpolate import RegularGridInterpolator
import time

start_time = time.time()

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
sc.lat = 180*np.arccos((2*np.random.random(Nthrow) - 1))/np.pi
sc.long = 360*np.random.random(Nthrow)

r_x_sc = (R + sc.altitude)*np.cos(np.radians(sc.lat))*np.cos(np.radians(sc.long))
r_y_sc = (R + sc.altitude)*np.cos(np.radians(sc.lat))*np.sin(np.radians(sc.long))
r_z_sc = (R + sc.altitude)*np.sin(np.radians(sc.lat))
r_sc = np.array([r_x_sc, r_y_sc, r_z_sc]).transpose()

#sc.lat = np.zeros(Nthrow)
#sc.long = np.zeros(Nthrow)


## NOTE: Thinking about changing the output of throwCR to be a cosmic ray object. But I need to create
## a cosmic ray class first. Sigh, later me problems. Or maybe I can find an undergrad to do this.

## throwCR will take in the radius of the planet and the number of cosmic rays thrown
## what it does it is uniformally sample points in the planet which will act as the 
## vertex of the cosmic ray interaction. It then samples a direction for the cosmic ray
## to be going.
CR_r0, CR_dir, CR_lat, CR_long = throwCR(R + 100, Nthrow)


## Check distance vertex is from the surface
b2 = CR_r0[:, 0]**2 + CR_r0[:, 1]**2 + CR_r0[:, 2]**2 - (CR_r0[:, 0]*CR_dir[:, 0] + CR_r0[:, 1]*CR_dir[:, 1] + CR_r0[:, 2]*CR_dir[:, 2])**2
b2max = np.max(b2)
b2min = np.min(b2)

## Create a mask for only those cosmic rays that are within 100 km of the surface
mask = (b2 < (R + 100)**2) & (b2 > (R - 100)**2) 

## Pass only those cosmic rays that are within 100 km of the surface to the projection function
cut = projectCRCone(sc, CR_r0[mask], CR_dir[mask], R, mask)


## Now we are only left with those cosmic rays that are within 100 km of the surface
## and that point their emission cone at the spacecraft
## At this point the CR_r0 and CR_dir are in cartesian coordinates
CR_r0 = CR_r0[mask][cut]
CR_dir = CR_dir[mask][cut]
r_sc = r_sc[mask][cut]

print(CR_r0.shape)
## Get the magnetic field at the location of the vertex interaction for each cosmic ray
## NOTE: Bfield_Earth_dipole is in spherical coordinates, so we need to convert the CR_r0 from cartesian to spherical coordinates to get the B field at the vertex
CR_r0_spherical = cartesian_to_spherical(CR_r0[:, 0], CR_r0[:, 1], CR_r0[:, 2])


B = Bfield_Earth_dipole(CR_r0_spherical[:, 0], CR_r0_spherical[:, 1], CR_r0_spherical[:, 2], R)



## Convert the B field from spherical to cartesian coordinates
B_cartesian = Fspherical_to_cartesian(B, CR_r0_spherical[:,0], CR_r0_spherical[:,1], CR_r0_spherical[:,2])

## Get the electric field at the location of the vertex interaction for each cosmic ray
E = Efield_simple(sc, CR_r0, B_cartesian, CR_dir)

theta_vB = np.arcsin(np.sqrt(np.sum(np.cross(CR_dir, B_cartesian)**2, axis=1))/np.sqrt(np.sum(B_cartesian**2, axis = 1)))*180/np.pi

mask = (theta_vB > 50)

rates = mask.astype(int)


## Mask off those events whos directiopns are too parallel to the local B field
E = E[mask]
CR_r0 = CR_r0[mask]
CR_dir = CR_dir[mask]
r_sc = r_sc[mask]

obs = CR_r0 - r_sc
#obs = obs/np.sqrt(np.sum(obs**2, axis = 1))

#print(obs, obs.shape)
#print(np.sqrt(np.sum(obs**2, axis = 1)), np.sqrt(np.sum(obs**2, axis = 1)).shape)


Acceptance = 4*np.pi**2*(R)**2*(np.sum(rates)/Nthrow)
#print(np.sum(rates)/Nthrow, Acceptance)
#print(2*np.pi*R*(2*100)*4*np.pi*(1.62*np.pi/180)*(0.01*np.pi/180))
#print(2*np.pi*69000*70*4*np.pi*(0.4*np.pi/180)*(0.02*np.pi/180))
end_time = time.time()
elapsed_time = end_time - start_time

#print(str(int(sys.argv[2])), str(sys.argv[3]))

data = pd.DataFrame(data={"Elapsed Time (s)": [elapsed_time], "Number Thrown": [Nthrow], "Number Accepted": [np.sum(rates)], "Planet Radius (km)": [R], "Altitude (km)": [sc.altitude], "Acceptance (km^2 sr)": [Acceptance]})
data.to_csv(str(sys.argv[3]) + '/Run' + str(int(sys.argv[2])) + '.csv')

if (int(sys.argv[4]) == 1):
    #CRdata = pd.DataFrame(data={"CR_x0": CR_r0[mask, 0][rates > 0], "CR_y0": CR_r0[mask, 1][rates > 0], "CR_z0": CR_r0[mask, 2][rates > 0], "CR_dir_x": CR_dir[mask, 0][rates > 0], "CR_dir_y": CR_dir[mask, 1][rates > 0], "CR_dir_z": CR_dir[mask, 2][rates > 0], "Accepted": rates[rates > 0]})
    #CRdata.to_csv(str(sys.argv[3]) + '/Run' + str(int(sys.argv[2])) + '_CRdata.csv')

    CRdata = pd.DataFrame(data={"CR_x0": CR_r0[:, 0], "CR_y0": CR_r0[:, 1], "CR_z0": CR_r0[:, 2], "CR_dir_x": CR_dir[:, 0], "CR_dir_y": CR_dir[:, 1], "CR_dir_z": CR_dir[:, 2], "Ex": E[:, 0], "Ey": E[:, 1], "Ez": E[:, 2], "obs_x": obs[:, 0], "obs_y": obs[:, 1], "obs_z": obs[:, 2], "Accepted": rates[rates > 0]})
    CRdata.to_csv(str(sys.argv[3]) + '/Run' + str(int(sys.argv[2])) + '_CRdata2.csv')

#print("Elapsed Time: ", elapsed_time)
