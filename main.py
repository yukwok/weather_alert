import os

from twilio.http.http_client import TwilioHttpClient

import requests
from twilio.rest import Client
import pprint

# # open weather map details  ---- use for cloud server
# api_key = os.environ.get("OWM_APIKEY")
# city = "shanghai"
# parameters = {
#     "appid": api_key,
#     "lat": 31.230391,
#     "lon": 121.473701,
#     "exclude": "current,minutely,daily"
# }
# # twillo details
# account_sid = "ACfc1f66926937dff5407161913da6f046"
# auth_token = os.environ.get("TWILLO_TOKEN")
# os.environ.get()
# #
# # TWILLO_TOKEN = 4f8e654118b63c378612a438f110034c
# #
# # OWM_APIKEY = 9f6959f38e1944621c0d10d01720caa5

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
# proxy_client = TwilioHttpClient(
#     proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

account_sid = "ACfc1f66926937dff5407161913da6f046"
auth_token = "8de9dae43f75ed764b3040487b2f0726"

client = Client(account_sid, auth_token)

weather_url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=weather_url, params=parameters)
data = response.json()
sliced_data = data['hourly'][:3]

pprint.pprint(sliced_data)

will_rain = False

for hour_data in sliced_data:
    weather_id = hour_data['weather'][0]['id']
    if weather_id < 600 and weather_id > 499:
        will_rain = True


print(will_rain)
if will_rain:
    print("will rain")
    message = client.messages \
        .create(
            body="Rain within 3 hrs, bring the urmbella",
            from_="+18303411303",
            to="+85290986832"
        )
    print(message.status)
