import numpy as np

def generateEfield(B, CR_r0, CR_dir, CR_lat, CR_long):
    ## velocity of the particle is the cosmic ray direction
    ## Assuming B is given in a x, y, z vector component
    ## perform cross product to get E-field vector

    ## B is a LUT that depends on the latitude and longitude
    ## Need to think about how to best incorporate this.

    ## Geomagnetic emission is a complicated process. For the sake
    ## of making life easy, the most import part is the v x B part
    ## as the emission has to go as v x B
    Ex = CR_dir[1]*B[2] - CR_dir[2]*B[1]
    Ey = -CR_dir[0]*B[2] + CR_dir[2]*B[0]
    Ez = CR_dir[0]*B[1] - CR_dir[1]*B[0]

    return (Ex, Ey, Ez)

    