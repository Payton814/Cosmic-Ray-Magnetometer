import numpy as np

def Bfield_Earth_dipole(r, latitude, longitude, R):
    B_r = 2*(R/r)**3 * (-31543*np.cos(latitude*np.pi/180) + np.sin(latitude*np.pi/180)*(2298*np.cos(longitude*np.pi/180) + 5922*np.sin(longitude*np.pi/180)))
    B_theta = -(R/r)**3 * (31543*np.sin(latitude*np.pi/180) + np.cos(latitude*np.pi/180)*(2298*np.cos(longitude*np.pi/180) + 5922*np.sin(longitude*np.pi/180)))
    B_phi = (R/r)**3 * (2298*np.sin(longitude*np.pi/180) - 5922*np.cos(longitude*np.pi/180))
    return np.array([B_r, B_theta, B_phi]).transpose()

def Fspherical_to_cartesian(F, r, theta, phi):
    Fx = F[0]*np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180) + F[1]*np.cos(theta*np.pi/180)*np.cos(phi*np.pi/180) - F[2]*np.sin(phi*np.pi/180)
    Fy = F[0]*np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180) + F[1]*np.cos(theta*np.pi/180)*np.sin(phi*np.pi/180) + F[2]*np.cos(phi*np.pi/180)
    Fz = F[0]*np.cos(theta*np.pi/180) - F[1]*np.sin(theta*np.pi/180)
    return np.array([Fx, Fy, Fz]).transpose()

