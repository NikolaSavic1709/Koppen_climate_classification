import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd
from matplotlib.colors import ListedColormap, BoundaryNorm

data = {
    'Longitude': [-120.5, 0.0, 45.0],
    'Latitude': [34.5, 15.0, 45.0],
    'Zone': [1,2,5]
}
df = pd.DataFrame(data)


worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))


fig, ax = plt.subplots(figsize=(12, 6)) # velicina mape
worldmap.plot(color="lightgrey", ax=ax) # boja pozadine kontinenata

x = df['Longitude']
y = df['Latitude']
z = df['Zone']

cmap=ListedColormap(np.array([(255, 50, 0), (255,255,0),(85, 255, 0),(0, 255, 191), (0, 94, 255)])/255.0)
scatter = plt.scatter(x, y, s=30, c=z, cmap=cmap)

cbar=plt.colorbar()
cbar.set_ticks([1.4, 2.2, 3.0, 3.8, 4.6])
cbar.set_ticklabels(['Tropical', 'Arid', 'Temperate', 'Cold continental', 'Polar'])

plt.xlim([-180, 180])
plt.ylim([-90, 90])

plt.title("Koppen climate classification")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()