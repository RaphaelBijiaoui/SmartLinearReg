import pandas as pd
import matplotlib as plt
df = pd.read_csv('autos.csv')
df['price']

ff = df[df['vehicleType'] == 'kombi']
gg = ff.groupby(['kilometer'])['price'].mean()
plt.plot(gg)
plt.show()

ff = df[df['vehicleType'] == 'kleinwagen']
gg = ff.groupby(['kilometer'])['price'].mean()
plt.plot(gg)
plt.show()

ff = df[df['vehicleType'] == 'limousine']
gg = ff.groupby(['kilometer'])['price'].mean()
plt.plot(gg)
plt.show()

ff = df[df['vehicleType'] == 'cabrio']
gg = ff.groupby(['kilometer'])['price'].mean()
plt.plot(gg)
plt.show()
