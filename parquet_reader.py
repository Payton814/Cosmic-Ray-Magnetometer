import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = "./corsika8/air_shower_test/profile.parquet"

df = pd.read_parquet(data)
print(df.head())

#print(df['X'], df['charged'])

plt.plot(np.array(df['X']), np.array(df['charged']), marker='o')


print(len(df['X']))
plt.xlim(0, 100)
plt.show()

