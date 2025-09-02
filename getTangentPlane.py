import numpy as np

## This function takes in the radius of a sphere and the latitude and longitude of a point on the sphere. 
## It then uses that to create a function for the tangent plane at that point on the spehre

## The tangent plane function is returned. 

## Remember, defining the origin as the center of the sphere, for the tangent plane function
## a positive value means above the plane (where positive is defined along radial unit vevtor)
## a negative value is below the plane
## 0 is on the plane. Due to numerical precision, a point in the plane can give a VERY small positive or negative value

def getTangentPlane(r, lat, long):
    x0 = r**2*np.sin(lat*np.pi/180)*np.cos(long*np.pi/180)
    y0 = r**2*np.sin(lat*np.pi/180)*np.sin(long*np.pi/180)
    z0 = r*np.cos(lat*np.pi/180)

    def f(x, y, z):
        return 2*x0*(x - x0) + 2*y0*(y - y0) + 2*z0*(z-z0)
    
    return f, (x0, y0, z0)