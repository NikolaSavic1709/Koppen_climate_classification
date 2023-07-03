import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd
from matplotlib.colors import ListedColormap, BoundaryNorm

zone_classes = {'Af': 1, 'Am': 1, 'As': 1, 'Aw': 1,
                'BSh': 2, 'BSk': 2, 'BWh': 2, 'BWk': 2,
                'Cfa': 3, 'Cfb': 3, 'Cfc': 3, 'Csa': 3, 'Csb': 3, 'Csc': 3, 'Cwa': 3, 'Cwb': 3, 'Cwc': 3,
                # okeanska, mediteranska, umereno kontinentalna
                'Dfa': 4, 'Dfb': 4, 'Dsa': 4, 'Dsb': 4, 'Dwa': 4, 'Dwb': 4,  # kontinentalna
                'Dfc': 5, 'Dfd': 5, 'Dsc': 5, 'Dsd': 5, 'Dwc': 5, 'Dwd': 5,  # subpolarna
                'EF': 6, 'ET': 6}  # polarna


def show_on_map(data):
    x = data[0]  # lon
    y = data[1]  # lat
    zone = data[2]
    worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

    fig, ax = plt.subplots(figsize=(12, 6))  # velicina mape

    worldmap.plot(color="lightgrey", ax=ax)  # boja pozadine kontinenata

    cmap = ListedColormap(
        np.array([(255, 50, 0), (255, 221, 0), (150, 255, 0), (0, 255, 170), (0, 208, 255), (0, 0, 255)]) / 255.0)
    plt.scatter(x, y, s=30, c=zone, cmap=cmap)

    cbar = plt.colorbar()
    cbar.set_ticks([1.4166667, 2.25, 3.083333, 3.91666667, 4.75, 5.583333])
    cbar.set_ticklabels(['Tropical', 'Arid', 'Temperate', 'Continental', 'Subarctic', 'Polar'])

    plt.xlim([-180, 180])
    plt.ylim([-90, 90])

    plt.title("Koppen climate classification")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    # manager = plt.get_current_fig_manager()
    # manager.full_screen_toggle()
    plt.show()


def main():
    points = []
    zones = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


    i = 0
    with open("../data/zones/weather_index_zones_5000.txt", 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) >= 3:
                # if values[2] != '/':
                zone_class = zone_classes[values[2]]
                zones[zone_class] += 1
                points.append((float(values[1]), float(values[0]), zone_class))
                i += 1
    print(zones)
    show_on_map(np.transpose(points))


if __name__ == '__main__':
    main()
