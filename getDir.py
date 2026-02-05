import numpy as np

def getDir(r0, N = 1):
    #print(r0)
    direc = []
    for iter in range(N):
        w = 99
        ## We want to make sure that the CR is going INTO the planet
        ## For this we need a direction that is below the tangent plane (i.e. w < 0)
        while (w > 0):
            ## Grab a random point on a unit sphere, centered on the cosmic ray entry point
            theta = 180*np.arccos((2*np.random.random() - 1))/np.pi
            phi = 360*np.random.random()

            ## Convert to the x, y, z value on the unit sphere
            x = np.sin(theta*np.pi/180)*np.cos(phi*np.pi/180)
            y = np.sin(theta*np.pi/180)*np.sin(phi*np.pi/180)
            z = np.cos(theta*np.pi/180)

            ## Check the direction of the cosmic ray
            ## If the cosmic ray tengent plane function returns a negative number, then we know that the
            ## cosmic ray is entering the planet
            #w = tp(x + r0[iter, 0], y + r0[iter, 1], z + r0[iter, 2], iter)

            ## To check if the samples direction is into the sphere
            ## take a dot product between dir and r_cr
            ## r_cr is the position of the CR from the center of planet
            ## if dir * r_cr is negative, then the direction is going into the planet
            w = x*r0[iter, 0] + y*r0[iter, 1] + z*r0[iter, 2]
            #w = -1
            #print(w.size)
            #print(y.size, r0[iter,1].size)
            #print(w)

        ## This just enforces that the returned vector is a unit vector
        ## I am pretty sure this is completely unnecesary since by definition
        ## x, y, z were sampled on unit sphere
        r = np.sqrt(x**2 + y**2 + z**2)
        direc.append(np.array([x/r, y/r, z/r]))
        

    return np.array(direc)