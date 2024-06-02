import requests

city = 'London'
url = "http://api.weatherapi.com/v1/current.json?key=ff559bef23aa43079de23918240206&q="+city+"&aqi=no"
response = requests.get(url)
weather_json = response.json()

# print(weather_json)

# temp = weather_json.get('current').get('temp_f')
temp = weather_json.get('current').get('temp_c')

# print(temp)

description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description, 'and', temp, 'degrees')