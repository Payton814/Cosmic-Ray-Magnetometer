import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#import scipy.interpolate
from scipy.interpolate import RegularGridInterpolator

file = open('./WMM2025COF/WMM2025COF/WMM.COF', 'r')


df = pd.read_csv('./linear_LUT.csv', header = None)
#print(df)
long = np.array(df.iloc[0, 1:])
lat = np.array(df.iloc[1:, 0])
B = np.array(df.iloc[1:, 1:])

print(lat)
X, Y = np.meshgrid(long, lat)

interp_func = RegularGridInterpolator((long, lat), B.T)

X_new, Y_new = np.meshgrid(long, lat)

# Evaluate interpolated values on new grid
points = np.array([X_new.ravel(), Y_new.ravel()]).T

print(points[0:5])
print(np.array([[0.0,0.0], [1.0,0.0]]))
Z_new = interp_func(points)
Z_new = Z_new.reshape(X_new.shape)
#print(Z_new)

# Plotting
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title('Original')
plt.pcolormesh(X, Y, B, shading='auto')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Interpolated')
plt.pcolormesh(X_new, Y_new, Z_new, shading='auto')
plt.colorbar()


plt.show()