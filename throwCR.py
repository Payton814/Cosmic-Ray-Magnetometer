import numpy as np
import pandas as pd
from spacecraft import spacecraft
from getTangentPlane import getTangentPlane
from getDir import getDir

CR_fov = 30 ## Atmospheres have permittivities very close to 1, so the cherenkov angle is extremely low
            ## but its still detectable off cone. For now say if within a 30 degree cone then its viewable
            ## This is based on nothing but just making a guess

def throwCR(sc):


    ## Literally just sampling if its on the same half of the world
    CR_latitude = sc.lat + 180*np.random.random(1) - 90
    CR_longitude = sc.long + 180*np.random.random(1) - 90

    ## Get the tangent plane function for the given lat and long
    tp, r0 = getTangentPlane(25559, CR_latitude, CR_longitude)

    ## Us eth
    dir = getDir(tp, r0)






    v = 3e8 ## For simplicity say CR traveling at speed of light, dont even care about energy

    return r0, dir, CR_latitude, CR_longitude








