import numpy as np
import pandas as pd
from spacecraft import spacecraft
from getTangentPlane import getTangentPlane
from getDir import getDir


def throwCR(sc, R, N = 1):


    ## Throw the cosmic ray at a random spot on the planet
    CR_latitude = 180*np.random.random(N)
    CR_longitude = 360*np.random.random(N)

    ## Get the tangent plane function for the given lat and long
    tp, r0 = getTangentPlane(R, CR_latitude, CR_longitude)

    ## Us eth
    direc = getDir(tp, r0, N)


    return r0, direc, CR_latitude, CR_longitude








