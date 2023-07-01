import os
import json
import random
import requests
import numpy as np
from map import show_on_map

api_key = os.environ.get('API_KEY')


def draw_map():
    folder_path = "../data/weather_index"  # Replace with the path to your folder
    map_data = [[], [], []]
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".json"):
            with open(file_path) as file:
                data = json.load(file)
                map_data[1].append(data["lat"])
                map_data[0].append(data["lon"])
                map_data[2].append(random.choice([1, 2, 3, 4, 5]))
    show_on_map(map_data)


def write_zones_into_file():
    folder_path = "../data/weather_index"
    map_data = [[], [], []]

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".json"):
            with open(file_path) as file:
                data = json.load(file)
                map_data[1].append(data["lat"])
                map_data[0].append(data["lon"])
                map_data[2].append(get_koppen_zone(data['lat'], data['lon']))

    with open("../data/zones/weather_index_zones.txt", "w") as file:
        for location in np.transpose(map_data):
            file.write(f"{location[1]},{location[0]},{location[2]}\n")


def get_koppen_zone(lat, lon):
    url = "https://koppen-climate-classification.p.rapidapi.com/classification"

    querystring = {"lat": lat, "lon": lon}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "koppen-climate-classification.p.rapidapi.com"
    }

    response_json = requests.get(url, headers=headers, params=querystring).json()
    # latitude = response_json["location"]["latitude"]
    # longitude = response_json["location"]["longitude"]
    if 'classification' in response_json:
        return response_json["classification"]
    else:
        print(lat,lon,response_json)
        return '/'




if __name__ == '__main__':
    # draw_map()
    write_zones_into_file()
