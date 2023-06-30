# import requests
#
# url = "https://weatherapi-com.p.rapidapi.com/current.json"
#
# querystring = {"q":"-29.50768, -54.69163"}
#
# headers = {
# 	"content-type": "application/octet-stream",
# 	"X-RapidAPI-Key": "b17d9df359msha9bf5b38e5b5dc5p12f47bjsna807f56a4a37",
# 	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())

import requests

url = "https://weatherapi-com.p.rapidapi.com/history.json"

querystring = {"q":"-22.272345186596755, -59.25903616327163","dt":"2023-04-28","lang":"en"}

headers = {
	"X-RapidAPI-Key": "b17d9df359msha9bf5b38e5b5dc5p12f47bjsna807f56a4a37",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())