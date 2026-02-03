import numpy as np

def projectCRCone(sc, CR_r0, CR_dir, R = 25362, mask = True):
    CR_theta = np.arccos(CR_dir[:,2])
    CR_phi = np.arctan(CR_dir[:,1]/CR_dir[:,0])

    ## Get the x, y, and z coordinates of the spacecraft in a planet centric view (i.e. origin at center of planet)
    sc_x = (R + sc.altitude)*np.sin(sc.lat[mask]*np.pi/180)*np.cos(sc.long[mask]*np.pi/180)
    sc_y = (R + sc.altitude)*np.sin(sc.lat[mask]*np.pi/180)*np.sin(sc.long[mask]*np.pi/180)
    sc_z = (R + sc.altitude)*np.cos(sc.lat[mask]*np.pi/180)

    ## Function that describes the surface of a cone with a vertex at x0, y0, z0
    ## opening angle alpha, and pointing in the theta, phi direction
    def f(x, y, z, x0, y0, z0, alpha, theta, phi):
        a = ((x - x0)*np.cos(phi) - (y - y0)*np.sin(phi))**2
        b = (((x - x0)*np.sin(phi) + (y - y0)*np.cos(phi))*np.cos(theta) - (z - z0)*np.sin(theta))**2
        c = (((x - x0)*np.sin(phi) + (y - y0)*np.cos(phi))*np.sin(theta) + (z - z0)*np.cos(theta))**2
        f = c*np.tan(alpha/2) - b - a
        return f
    
    ## Equation of a cone is going to give forward and backward cone with the vertex
    ## at the point of the CR.
    ## The emission forward directed so we want to check that not only are we in the cone, but that we are 
    ## in the forward direction
    forwardCone = CR_dir[:,0]*(sc_x - CR_r0[:,0]) + CR_dir[:,1]*(sc_y - CR_r0[:,1]) + CR_dir[:,2]*(sc_z - CR_r0[:,2])
    
    ## While the emission wavefront collowing along a curve, off cone events lower the incident power
    ## Therefore we create 2 cones that decribe how far off cone in either direction we can see.
    outerCone = f(sc_x, sc_y, sc_z, CR_r0[:,0], CR_r0[:,1], CR_r0[:,2], (1.62 + 0.01)*np.pi/180, CR_theta, CR_phi)
    innerCone = f(sc_x, sc_y, sc_z, CR_r0[:,0], CR_r0[:,1], CR_r0[:,2], (1.62 - 0.01)*np.pi/180, CR_theta, CR_phi)

    return ((outerCone > 0) & (innerCone < 0) & (forwardCone > 0))

    '''if (outerCone > 0 and innerCone < 0 and forwardCone > 0):
        return 1
    else:
        return 0'''