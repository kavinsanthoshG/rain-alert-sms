import requests
import os
from twilio.rest import Client
MY_KEY="93cca5ff4e84438b982124013222510"
account_sid = "ACcd11533bd230f3886b84d4fa62f4b7d5
auth_token = "40610c65bb503d08f843eec3918dd2f0"
paramater={
    "key":MY_KEY,
     "q":"Chennai",
     "days":"no",
     "alerts":"no"

}
API_KEY="93cca5ff4e84438b982124013222510"
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
        from_="+12284600163",
        to='+919360509799'
    )


    print(message.status)
# print("Printed")





