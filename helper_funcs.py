import numpy as np

## Converts cartesian coordinates to spherical coordinates
def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/r) * 180/np.pi
    phi = np.arctan2(y, x) * 180/np.pi
    return np.array([r, theta, phi]).transpose()

## Converts spherical coordinates to cartesian coordinates
def spherical_to_cartesian(r, theta, phi):
    x = r*np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180)
    y = r*np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180)
    z = r*np.cos(theta*np.pi/180)
    return np.array([x, y, z]).transpose()


## Converts spherical coordinate vector field to cartesian coordinate field
def Fspherical_to_cartesian(F, r, theta, phi):
    Fx = F[:, 0]*np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180) + F[:, 1]*np.cos(theta*np.pi/180)*np.cos(phi*np.pi/180) - F[:, 2]*np.sin(phi*np.pi/180)
    Fy = F[:, 0]*np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180) + F[:, 1]*np.cos(theta*np.pi/180)*np.sin(phi*np.pi/180) + F[:, 2]*np.cos(phi*np.pi/180)
    Fz = F[:, 0]*np.cos(theta*np.pi/180) - F[:, 1]*np.sin(theta*np.pi/180)
    return np.array([Fx, Fy, Fz]).transpose()