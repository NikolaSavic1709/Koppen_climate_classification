import datetime

import numpy as np
from shapely.geometry import Polygon, Point
from sklearn.cluster import KMeans
from map import show_on_map, main
import random


def get_uniform_points_for_continent(file_path, point_count):
    bounds = []

    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) >= 2:
                bounds.append((float(values[0]), float(values[1])))
    polygon = Polygon(bounds)

    points = []
    while len(points) < 10 * point_count:
        point = (np.random.uniform(polygon.bounds[0], polygon.bounds[2]),
                 np.random.uniform(polygon.bounds[1], polygon.bounds[3]))
        if polygon.contains(Point(point)):
            points.append(point)

    X = np.array(points)
    kmeans = KMeans(n_clusters=point_count, n_init=100).fit(X)
    centroids = kmeans.cluster_centers_

    with open("../data/uniform_points_5000.txt", "a") as file:
        for centroid in centroids:
            file.write(str(centroid[0]) + ',' + str(centroid[1]))
            file.write("\n")
    print(datetime.datetime.now(), file_path, "finished")


def get_uniform_points():
    get_uniform_points_for_continent("../data/boundaries/north_america.txt", 1000)
    get_uniform_points_for_continent("../data/boundaries/south_america.txt", 550)
    get_uniform_points_for_continent("../data/boundaries/australia.txt", 250)
    get_uniform_points_for_continent("../data/boundaries/euroasia.txt", 2175)
    get_uniform_points_for_continent("../data/boundaries/africa.txt", 1025)
    # main()
    # show_on_map(np.transpose(points))


if __name__ == '__main__':
    get_uniform_points()
