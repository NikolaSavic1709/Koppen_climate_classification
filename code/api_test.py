import requests
import os

# Access a specific environment variable
api_key = os.environ.get('API_KEY')

# url = "https://weatherapi-com.p.rapidapi.com/history.json"
#
# querystring = {"q":"-1.328882860515801,-76.62785482600087","dt":"2023-06-22","lang":"en"}
#
# headers = {
# 	"X-RapidAPI-Key": api_key,
# 	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())


#
#
# url = "https://koppen-climate-classification.p.rapidapi.com/classification"
#
# querystring = {"lat":"54.98","lon":"-3.68"}
#
# headers = {
# 	"X-RapidAPI-Key": api_key,
# 	"X-RapidAPI-Host": "koppen-climate-classification.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())