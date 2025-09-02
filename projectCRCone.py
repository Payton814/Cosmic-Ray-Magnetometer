import numpy as np

def projectCRCone(sc, CR_r0, CR_dir):
    CR_theta = np.arccos(CR_dir[2])
    CR_phi = np.arctan(CR_dir[1]/CR_dir[0])

    sc_x = 26559*np.sin(sc.lat*np.pi/180)*np.cos(sc.long*np.pi/180)
    sc_y = 26559*np.sin(sc.lat*np.pi/180)*np.sin(sc.long*np.pi/180)
    sc_z = 26559*np.cos(sc.lat*np.pi/180)

    def f(x, y, z, x0, y0, z0, alpha, theta, phi):
        a = ((x - x0)*np.cos(phi) - (y - y0)*np.sin(phi))**2
        b = (((x - x0)*np.sin(phi) + (y - y0)*np.cos(phi))*np.cos(theta) - (z - z0)*np.sin(theta))**2
        c = (((x - x0)*np.sin(phi) + (y - y0)*np.cos(phi))*np.sin(theta) + (z - z0)*np.cos(theta))**2
        f = c*np.tan(alpha/2) - b - a
        return f
    
    forwardCone = CR_dir[0]*(sc_x - CR_r0[0]) + CR_dir[1]*(sc_y - CR_r0[1]) + CR_dir[2]*(sc_z - CR_r0[2])
    
    cone = f(sc_x, sc_y, sc_z, CR_r0[0], CR_r0[1], CR_r0[2], 4*np.pi/180, CR_theta, CR_phi)
    if (cone > 0 and forwardCone > 0):
        return 1
    else:
        return 0