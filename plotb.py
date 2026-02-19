import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Ntrig = 0
Nthrow = 0
Nt = []

for i in range(8000):
    for ii in range(1):
        try:
            df = pd.read_csv("./simulation_data/sim" + f"{i:05d}" + "/Run" + str(ii+1) + "/Run" + str(ii+1) + ".csv")
            Ntrig = Ntrig + int(df["Number Accepted"][0])
            Nt.append(int(df["Number Accepted"][0]))
            Nthrow = Nthrow + int(df["Number Thrown"][0])
        except:
            print("Missing: " + "./simulation_data/sim" + f"{i:05d}" + "/Run" + str(ii+1) + "/Run" + str(ii+1) + ".csv")

print("Total Thrown: ", Nthrow)
print("Total Triggered: ", Ntrig)
print("Acceptance: ", (Ntrig/Nthrow)*4*np.pi**2*(25362)**2, " km^2 sr")
print("Acceptance Paper", (2*np.pi*25362*200)*4*np.pi*(1.62*np.pi/180)*(0.01*np.pi/180), " km^2 sr")

bins = np.arange(min(Nt), max(Nt) + 1, 1)
plt.hist(Nt, bins = bins)
plt.savefig("hist4.png")