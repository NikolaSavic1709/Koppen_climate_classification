import numpy as np
from shapely.geometry import Polygon, Point
from sklearn.cluster import KMeans

# Define the polygon that approximates the shape of Asia
south_america_polygon = Polygon([
    (-50.5669506, -75.2042429),
    (-55.0259174, - 72.2159616),
    (-55.3270555, - 65.3604929),
    (-51.19898, - 68.8287469),
    (-47.7287568, - 65.9219562),
    (-39.1612939, - 62.3722116),
    (-38.3387761, - 58.1534616),
    (-29.0444865, - 48.7858124),
    (-24.3989266, - 47.2554849),
    (-24.4438068, - 42.6847116),
    (-4.4741957, - 34.0714304),
    (0.0915626, - 49.1886179),
    (4.4815173, - 50.7706491),
    (12.300656, - 70.9854929),
    (7.9758342, - 77.3136179),
    (-4.64942, - 81.8839304),
    (-13.8345145, - 77.1378366),
    (-18.7260244, - 70.2823679),
    (-50.5669506, - 75.2042429)  # southwest corner
])

# Define the number of points to generate
n_points = 10


# Generate random points within the polygon
points = []
while len(points) < 6 * n_points:
    point = (np.random.uniform(south_america_polygon.bounds[0], south_america_polygon.bounds[2]),
             np.random.uniform(south_america_polygon.bounds[1], south_america_polygon.bounds[3]))
    if south_america_polygon.contains(Point(point)):
        points.append(point)

# Use k-means clustering to generate uniformly distributed points
# for centroid in points:
#     print((centroid[0], centroid[1]))
# print("-------------")
X = np.array(points)
kmeans = KMeans(n_clusters=n_points, n_init=100).fit(X)
centroids = kmeans.cluster_centers_

# Print the resulting points
for centroid in centroids:
    print((centroid[0], centroid[1]))

# import numpy as np
# from sklearn.cluster import KMeans
#
# # Define the bounds of Asia in terms of latitude and longitude
# lat_min, lat_max = 10.0, 80.0
# lng_min, lng_max = 25.0, 170.0
#
# # Generate 10,000 random points within the bounds of Asia
# n_points = 10000
# lats = np.random.uniform(low=lat_min, high=lat_max, size=n_points)
# lngs = np.random.uniform(low=lng_min, high=lng_max, size=n_points)
# points = np.column_stack((lats, lngs))
#
# # Use k-means clustering to cluster the random points into 490 clusters
# n_clusters = 10
# kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=0).fit(points)
#
# centers = kmeans.cluster_centers_
#
# # Print the resulting centers
# for center in centers:
#     print(center)


# import numpy as np
# from shapely.geometry import Polygon, Point
#
# # Define the polygon that approximates the shape of Asia
# south_america_polygon = Polygon([
#     (68.0, 25.0), # northwest corner
#     (55.0, 96.0), # northeast corner
#     (9.0, 104.0), # southeast corner
#     (0.0, 36.0)   # southwest corner
# ])
#
# # Define the number of points to generate
# n_points = 490
#
# # Generate uniformly distributed points within the polygon
# points = []
# while len(points) < n_points:
#     point = Point(np.random.uniform(south_america_polygon.bounds[0], south_america_polygon.bounds[2]),
#                   np.random.uniform(south_america_polygon.bounds[1], south_america_polygon.bounds[3]))
#     if south_america_polygon.contains(point):
#         points.append((point.y, point.x))
#
# # Print the resulting points
# for point in points:
#     print(point)
