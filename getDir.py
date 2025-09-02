import numpy as np

def getDir(f, r0):

    w = 99
    ## We want to make sure that the CR is going INTO the planet
    ## For this we need a direction that is below the tangent plane (i.e. w < 0)
    while (w > 0):
        ## Grab a random point on a unit sphere
        theta = 180*np.random.random()
        phi = 360*np.random.random()

        ## Convert to the x, y, z value on the unit sphere
        x = np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180)
        y = np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180)
        z = np.cos(theta*np.pi/180)

        w = f(x + r0[0], y + r0[1], z + r0[2])

    r = np.sqrt(x**2 + y**2 + z**2)

    return (x/r, y/r, z/r)