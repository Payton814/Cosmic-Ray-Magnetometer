from spacecraft import spacecraft
import numpy as np

def updateSC(sc):
    sc.lat = 180*np.acos((2*np.random.random() - 1))/np.pi
    sc.long = 360*np.random.random()
    #a = np.random.random()
    #if (a > 0.5):
    #    sc.long = 180
    #else:
    #    sc.long = 0