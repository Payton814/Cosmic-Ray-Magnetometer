import numpy as np
import pandas as pd

Ntrig = 0
Nthrow = 0

for i in range(100):
    for ii in range(10):
        try:
            df = pd.read_csv("./simulation_data/sim" + f"{i:05d}" + "/Run" + str(ii+1) + "/Run" + str(ii+1) + ".csv")
            Ntrig = Ntrig + int(df["Number Accepted"][0])
            Nthrow = Nthrow + int(df["Number Thrown"][0])
        except:
            print("Missing: " + "./simulation_data/sim" + f"{i:05d}" + "/Run" + str(ii+1) + "/Run" + str(ii+1) + ".csv")

print("Total Thrown: ", Nthrow)
print("Total Triggered: ", Ntrig)
print("Acceptance: ", (Ntrig/Nthrow)*16*np.pi**2*(25362)**2, " km^2 sr")
print("Acceptance Paper", (2*np.pi*25362*200)*4*np.pi*(1.62*np.pi/180)*(0.01*np.pi/180), " km^2 sr")

