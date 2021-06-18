import requests
from twilio.rest import Client

# open weather map details
api_key = "9f6959f38e1944621c0d10d01720caa5"
city = "Shanghai"
parameters = {
    "appid": api_key,
    "lat": 31.230391,
    "lon": 121.473701,
    "exclude": "current,minutely,daily"
}
# twillo details
account_sid = "ACfc1f66926937dff5407161913da6f046"
auth_token = "4f8e654118b63c378612a438f110034c"

weather_url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=weather_url, params=parameters)
data = response.json()
sliced_data = data['hourly'][:12]

will_rain = False

for hour_data in sliced_data:
    weather_id = hour_data['weather'][0]['id']
    if weather_id < 800:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    print("will rain")
    message = client.messages \
        .create(
        body="Bring the urmbella",
        from_="+18303411303",
        to="+85290986832"
    )
    print(message.status)