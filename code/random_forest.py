import json
import random

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from map import zone_classes, show_on_map
from joblib import dump, load
from metrics import *

points = []
scaler = None


def create_model(x_train, y_train, n_estimators, max_depth, min_samples_split, min_samples_leaf, class_weight):
    global scaler
    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train_scaled = scaler.transform(x_train)

    rf_classifier = RandomForestClassifier(n_estimators=n_estimators,
                                           max_depth=max_depth,
                                           min_samples_split=min_samples_split,
                                           min_samples_leaf=min_samples_leaf,
                                           class_weight=class_weight)

    rf_classifier.fit(x_train_scaled, y_train)
    # rf_classifier.fit(x_train, y_train)
    dump(rf_classifier, '../data/model/test_model.joblib')


def predict(x_test):
    rf_classifier = load('../data/model/test_model.joblib')
    global scaler
    x_test_scaled = scaler.transform(x_test)
    predictions = rf_classifier.predict(x_test_scaled)
    # predictions = rf_classifier.predict(x_test)
    return predictions


def get_zone_by_location(lat, lon):
    for point in points:
        if point[0] == lat and point[1] == lon:
            if point[2] == '/':
                return 'ET'
            return point[2]


def prepare_data(hours_frequency, location_weight, temperature_weight, test_size):
    random_numbers = random.sample(range(5000), test_size)
    x_train = []
    y_train = []
    x_test = []
    true_values = []
    for i in range(0, 5000):
        # for i in range(index1, index2):
        file_path = "../data/weather_index_5000/" + str(i + 1) + ".json"
        try:
            with open(file_path) as file:
                location_data = []
                data = json.load(file)
                location_data.append(data["lat"] * location_weight)
                location_data.append(data["lon"] * location_weight)
                location_data.append(data["sunrise"])
                location_data.append(data["sunset"])
                for hour in data['weather']:
                    if hour['hour'] % hours_frequency == 0:
                        location_data.append(hour["temp_c"] * temperature_weight)
                        location_data.append(hour["wind_kph"])
                        location_data.append(hour["pressure_mb"])
                        location_data.append(hour["precip_mm"])
                        location_data.append(hour["humidity"])
                if i not in random_numbers:
                # if i>1799 or i<1550:
                    x_train.append(location_data)
                    y_train.append(zone_classes[get_zone_by_location(data["lat"], data["lon"])])
                else:
                    x_test.append(location_data)
                    true_values.append(zone_classes[get_zone_by_location(data["lat"], data["lon"])])
        except Exception as e:
            continue
    return x_train, y_train, x_test, true_values


def read_zones():
    with open("../data/zones/weather_index_zones_5000.txt", 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) >= 3:
                points.append((float(values[0]), float(values[1]), values[2]))


def prepare_map(x_train, y_train, x_test, predictions):
    data_for_map = [[], [], []]
    for i in range(len(x_train)):
        data_for_map[0].append(x_train[i][1])
        data_for_map[1].append(x_train[i][0])
        data_for_map[2].append(y_train[i])
    for i in range(len(x_test)):
        data_for_map[0].append(x_test[i][1])
        data_for_map[1].append(x_test[i][0])
        data_for_map[2].append(predictions[i])
    show_on_map(data_for_map)


def test():
    hour_frequency = 3
    location_weight = 1
    temperature_weight = 1
    test_sizes = [500]  # 200, 1000
    n_estimators = [400]  # 100, 200
    max_depths = [None]
    min_samples_splits = [2]  # 5 10
    min_samples_leafs = [1]  # 5
    class_weights = [{1: 1 / 870, 2: 1 / 1291, 3: 1 / 684, 4: 1 / 449, 5: 1 / 965,
                      6: 1 / 532}]  # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1},
    for n_estimator in n_estimators:
        for max_depth in max_depths:
            for min_samples_split in min_samples_splits:
                for min_samples_leaf in min_samples_leafs:
                    for class_weight in class_weights:
                        for test_size in test_sizes:
                            x_train, y_train, x_test, true_values = prepare_data(hour_frequency, location_weight,
                                                                                 temperature_weight, test_size)
                            create_model(x_train, y_train, n_estimator, max_depth, min_samples_split,
                                         min_samples_leaf, class_weight)
                            predictions = predict(x_test)

                            print("Tacnost:", calculate_accuracy(predictions, true_values))
                            print("Preciznost:", calculate_precision(predictions, true_values))
                            print("Odziv:", calculate_recall(predictions, true_values))
                            return x_train, y_train, x_test, predictions


if __name__ == '__main__':
    read_zones()
    # test()
    a, b, c, d = test()
    prepare_map(a, b, c, d)
