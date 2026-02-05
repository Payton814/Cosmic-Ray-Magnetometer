import numpy as np
import pandas as pd
from spacecraft import spacecraft
from getTangentPlane import getTangentPlane
from getDir import getDir


def throwCR(R, N = 1):


    ## Throw the cosmic ray at a random spot on the uniform sphere
    CR_latitude = 180*np.arccos((2*np.random.random(N) - 1))/np.pi ## This is because when sampling latitude, we need to be uniform in cosine
    CR_longitude = 360*np.random.random(N)
    CR_vertex = R*(np.random.random(N)**(1/3))  ## Uniform in r^3 to get uniform in volume

    ## Take the radius, latitude and longitude, and convert into a x, y, z point in the sphere 
    x0 = CR_vertex*np.sin(CR_latitude*np.pi/180)*np.cos(CR_longitude*np.pi/180)
    y0 = CR_vertex*np.sin(CR_latitude*np.pi/180)*np.sin(CR_longitude*np.pi/180)
    z0 = CR_vertex*np.cos(CR_latitude*np.pi/180)

    r0 = np.array([x0, y0, z0]).transpose()

    ## Get the tangent plane function for the given lat and long
    #tp, r0 = getTangentPlane(R, CR_latitude, CR_longitude)

    ## Us eth
    direc = getDir(r0, N)


    return r0, direc, CR_latitude, CR_longitude








