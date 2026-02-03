import numpy as np
import pandas as pd
from spacecraft import spacecraft
from getTangentPlane import getTangentPlane
from getDir import getDir


def throwCR(sc, R):


    ## Throw the cosmic ray at a random spot on the planet
    CR_latitude = 180*np.random.random(1)
    CR_longitude = 360*np.random.random(1)

    ## Get the tangent plane function for the given lat and long
    tp, r0 = getTangentPlane(R, CR_latitude, CR_longitude)

    ## Us eth
    dir = getDir(tp, r0)


    return r0, dir, CR_latitude, CR_longitude








