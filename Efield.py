import numpy as np

def  Efield_simple(sc, CR_r0, B, v):
    ## The electric field from a geomagnetic shower is going to be polarized in the direction of v x B
    E = np.cross(v, B)

    return E

