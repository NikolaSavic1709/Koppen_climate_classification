import json
import os

import numpy as np


def get_missed_indexes():
    folder_path = "../data/weather_index_5000"  # Replace with the path to your folder
    # Iterate over each file in the folder
    a = []
    for filename in os.listdir(folder_path):
        a.append(int(filename.split('.')[0]))

    a_set = set(a)

    all_numbers_set = set(range(1, 5001))

    not_present_set = all_numbers_set - a_set

    not_present_list = list(not_present_set)
    not_present_list.sort()
    print(not_present_list)


def sort_zones():
    map_data = [[], [], []]

    for i in range(2000):
        file_path = "../data/weather_index/"+ str(i + 1) + ".json"
        try:
            with open(file_path) as file:
                data = json.load(file)
                map_data[1].append(data["lat"])
                map_data[0].append(data["lon"])
                val=get_from_unsorted_zones(data["lat"], data["lon"])
                map_data[2].append(val)
        except Exception:
            print(i)
            continue

    with open("../data/zones/weather_index_zones_sorted.txt", "w") as file:
        for location in np.transpose(map_data):
            file.write(f"{location[1]},{location[0]},{location[2]}\n")


points = []


def get_from_unsorted_zones(lat, lon):
    for tuple_value in points:
        if tuple_value[1] == lat and tuple_value[0] == lon:
            return tuple_value[2]


def read_unsorted():
    with open("../data/zones/weather_index_zones.txt", 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) >= 3:
                if values[2] != '/':
                    points.append((float(values[1]), float(values[0]), values[2]))


if __name__ == "__main__":
    read_unsorted()
    sort_zones()
