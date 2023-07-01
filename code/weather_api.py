import requests
import os
import json
import time

api_key = os.environ.get('API_KEY')

url = "https://weatherapi-com.p.rapidapi.com/history.json"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}


def get_timestamps_avg(timestamps):
    res = 0
    total_count = len(timestamps)
    for timestamp in timestamps:
        if ':' not in timestamp or ' ' not in timestamp:
            total_count -= 1
        else:
            hour, minutes = timestamp.split(':')
            minutes, period = minutes.split(' ')
            res += int(hour) * 60 + int(minutes)
            if period == 'PM':
                res += 12 * 60
    return res // total_count


def get_avg_data(responses, location):
    sunrises = []
    sunsets = []
    hourly_avg = []
    for _ in range(24):
        hourly_avg.append({
            "hour": 0,
            "temp_c": 0,
            "is_day": 0,
            "wind_kph": 0,
            "pressure_mb": 0,
            "precip_mm": 0,
            "humidity": 0,
            "cloud": 0,
            "feelslike_c": 0,
            "will_it_rain": 0,
            "chance_of_rain": 0,
            "will_it_snow": 0,
            "chance_of_snow": 0,
            "vis_km": 0,
            "gust_kph": 0,
            "uv": 0
        })
    for response in responses:
        data = response['forecast']['forecastday'][0]
        sunrises.append(data['astro']['sunrise'])
        sunsets.append(data['astro']['sunset'])
        for hour in range(24):
            hourly_avg[hour]["hour"] = hour
            hourly_avg[hour]["temp_c"] += float(data['hour'][hour]['temp_c']) / len(responses)
            hourly_avg[hour]["is_day"] += float(data['hour'][hour]['is_day']) / len(responses)
            hourly_avg[hour]["wind_kph"] += float(data['hour'][hour]['wind_kph']) / len(responses)
            hourly_avg[hour]["pressure_mb"] += float(data['hour'][hour]['pressure_mb']) / len(responses)
            hourly_avg[hour]["precip_mm"] += float(data['hour'][hour]['precip_mm']) / len(responses)
            hourly_avg[hour]["humidity"] += float(data['hour'][hour]['humidity']) / len(responses)
            hourly_avg[hour]["cloud"] += float(data['hour'][hour]['cloud']) / len(responses)
            hourly_avg[hour]["feelslike_c"] += float(data['hour'][hour]['feelslike_c']) / len(responses)
            hourly_avg[hour]["will_it_rain"] += float(data['hour'][hour]['will_it_rain']) / len(responses)
            hourly_avg[hour]["chance_of_rain"] += float(data['hour'][hour]['chance_of_rain']) / len(responses)
            hourly_avg[hour]["will_it_snow"] += float(data['hour'][hour]['will_it_snow']) / len(responses)
            hourly_avg[hour]["chance_of_snow"] += float(data['hour'][hour]['chance_of_snow']) / len(responses)
            hourly_avg[hour]["vis_km"] += float(data['hour'][hour]['vis_km']) / len(responses)
            hourly_avg[hour]["gust_kph"] += float(data['hour'][hour]['gust_kph']) / len(responses)
            hourly_avg[hour]["uv"] += float(data['hour'][hour]['uv']) / len(responses)

    avg_json = {
        'name': location['name'],
        'region': location['region'],
        'country': location['country'],
        'lat': location['lat'],
        'lon': location['lon'],
        'sunrise': get_timestamps_avg(sunrises),
        'sunset': get_timestamps_avg(sunsets),
        "weather": hourly_avg
    }

    return avg_json


def collect_data_for_location(lat, lon,index):
    dates = ["2023-06-23", "2023-06-24", "2023-06-25", "2023-06-26", "2023-06-27", "2023-06-28",
             "2023-06-29", "2023-06-30"]
    location = {'name': 'unknown'}
    responses = []
    try:
        for date in dates:
            querystring = {"q": lat + ',' + lon, "dt": date, "lang": "en"}
            response_json = requests.get(url, headers=headers, params=querystring).json()
            if not 'location' in response_json:
                return
            location = response_json['location']
            responses.append(response_json)
        avg_json = get_avg_data(responses, location)
        location_name = location['name']
        with open("../data/weather_index/" + str(index) + '.json', "w") as file:
            json.dump(avg_json, file)
    except Exception as e:
        print(e)
        print(location, lat, lon)


def collect_weather_data():
    i = 0
    with open("../data/uniform_points.txt", 'r') as file:
        for line in file:
            i += 1
            values = line.strip().split(',')
            if len(values) >= 2 and i not in [568,1716,1931,1987]:
                collect_data_for_location(values[1], values[0],i)

if __name__ == '__main__':
    # collect_data_for_location('45', '21')
    collect_weather_data()
