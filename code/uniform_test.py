import numpy as np
from shapely.geometry import Polygon, Point
from sklearn.cluster import KMeans
from map import show_on_map
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
    while len(points) < 5 * point_count:
        point = (np.random.uniform(polygon.bounds[0], polygon.bounds[2]),
                 np.random.uniform(polygon.bounds[1], polygon.bounds[3]))
        if polygon.contains(Point(point)):
            points.append(point)

    X = np.array(points)
    kmeans = KMeans(n_clusters=point_count, n_init=100).fit(X)
    centroids = kmeans.cluster_centers_

    expanded_centroids = []

    for centroid in centroids:
        expanded_centroid = np.append(centroid, random.choice([1, 2, 3, 4, 5]))
        expanded_centroids.append(expanded_centroid)

    return expanded_centroids


def get_uniform_points():
    points=get_uniform_points_for_continent("../data/borders/north_america.txt", 36)+get_uniform_points_for_continent("../data/borders/south_america.txt", 26)+get_uniform_points_for_continent("../data/borders/australia.txt", 12)+get_uniform_points_for_continent("../data/borders/euroasia.txt", 81)+get_uniform_points_for_continent("../data/borders/africa.txt", 45)

    show_on_map(np.transpose(points))


if __name__ == '__main__':
    get_uniform_points()
