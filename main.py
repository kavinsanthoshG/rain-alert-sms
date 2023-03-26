import requests
import os
from twilio.rest import Client
MY_KEY=""
account_sid = ""
auth_token = ""
paramater={
    "key":MY_KEY,
     "q":"Chennai",
     "days":"no",
     "alerts":"no"

}
API_KEY=""
response=requests.get(url="https://api.weatherapi.com/v1/forecast.json",params=paramater)
response.raise_for_status()
data=response.json()
toBeSliced=data["forecast"]["forecastday"][0]["hour"]
toBeSliced=toBeSliced[:13]

willRain=False

for a in toBeSliced:
    # print(a)
    if a["will_it_rain"]==1:
        willRain=True




if willRain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is going to Rain within the next 12 hours! Take Umbrella 🌂    ☂    ☔",
        from_="+12",
        to='+91'
    )


    print(message.status)
# print("Printed")





