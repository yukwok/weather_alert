import requests

api_key = "9f6959f38e1944621c0d10d01720caa5"
city = "Shanghai"
parameters = {
    "appid": api_key,
    "q": city
}
weather_url = "api.openweathermap.org/data/2.5/weather"

response = requests.get(url=weather_url, params=parameters)
print(response)



