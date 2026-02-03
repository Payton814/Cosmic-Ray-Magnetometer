import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

Ru = 25537e3 ##m

b = [Ru]
X = []
b = np.linspace(Ru, Ru + 150e3, 1000)

for i in range(len(b)):
    def density(r):
        return 0.47*np.exp(-(r - Ru)/30e3)*r/(np.sqrt(r**2 - b[i]**2+0.01))

    I = quad(density, b[i], np.inf) ## This answer is in kg/m^2
    X.append(I[0]*0.1)

#def density(r):
#    return 0.47*np.exp(-(r - Ru)/30e3)*r/(np.sqrt(r**2 - Ru**2 + 1e-3))

#I = 2*quad(density, Ru, np.inf) ## This answer is in kg/m^2
#print(I[0]*0.1)
plt.plot((b - Ru)/1e3, X)
plt.xlabel('Altitude [km]')
plt.ylabel('X [g/cm^2]')
plt.axhline(1500, color = 'k')
plt.grid()
plt.show()
