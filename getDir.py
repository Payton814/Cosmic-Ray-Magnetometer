import numpy as np

def getDir(r0, N = 1):
    theta_dir = np.arccos(2*np.random.random(N) - 1)
    phi_dir = 2*np.pi*np.random.random(N)

    r_dir = np.array([np.sin(theta_dir)*np.cos(phi_dir), np.sin(theta_dir)*np.sin(phi_dir), np.cos(theta_dir)]).transpose()
        

    return r_dir