# 🌧️ ⛈️ Rain Alert through SMS Application ✉️➡📱

Checks Whether Rain can be expected in a Target Location in the next 12 hours. If it is forecasted to Rain,sends an SMS to User's Smart Phone.
![A Man getting to know that it is going to rain today through his Smartphone](DALL%C2%B7E%202023-03-25%2019.13.05%20-%20a%20man%20finding%20out%20that%20is%20going%20to%20rain%20today%20through%20his%20phoen.png)

## General Project Details:

**main.py Explanation:**

API End Point from where Forecasted Weather Data is acquired for a Specific Customizable Location in the next 12 Hours: https://api.weatherapi.com/v1/forecast.json

The Acquired Data is processed to find whether it's gonna Rain in the next 12 hours.

If it doesn't Rain the Server Stops.

If it's gonna Rain, the Server sends a Customizable Message to the User's specified Mobile Number.

It uses Twilio SMS API, to send a Customized Message from a API's Mobile Number to the User's Mobile Number.

Then the Server Ends.

The Script in the main.py file is hosted on https://www.pythonanywhere.com/.( A free Script Hosting and Executing Service at a Predefined time - Daily or Simple a Free Server)

In the pythonanywhere,the Script is configured to run at Early Morning 6 A.M..

## Customize the Software for your Location and your Device

**How to Run the Rain Alert SMS Application for your Location and for your Mobile Number?**

Assumming you know how to download the Project as Zip and Extract.

1.Go to the www.weatherapi.com and create your Account.(Free account has access for just 15 days. So, it is recommended to Create a Paid Account).

2.Then Generate an API Key and go to the main.py and change the value of MY_KEY and API_KEY(14th line) variable to your API key as a String.

ex:

MY_KEY="Your API Key inside Double Cotation"

3. Create an Account at Twilio SMS API, generate account_sid and auth_token.

change account_sid and auth_token variables to your sid and token.

4. In the Parameter Dictionary, **change key 'q' to your Location**. This makes the Application to check whether if it is going to rain for your Location. Just type your City's name.

5. Go to the Bottom of the file
   you will find this Script

**message = client.messages.create(
body="Type your message",
from\_="Type the Number from your Twilio SMS API account",
to='Type the Mobile Number where you want to receive Rain Alert'
)**

**⚠️Important⚠️**
from="Twilio's Number" is where you get your SMS from Twilio and it will be available in your Twilio account.

6. After this Create a Account in www.pythonanywhere.com.

7. Copy the Script in main.py to your Server and Configure the Server to work at 6 A.M. everyday, if you are doing a 9 to 5 Job.

8. And the Server checks whether if it is going to rain in the next 12 hours. i.e. upto 6 P.M. in the Evening and sends you a message if it does. So, that you can take your Umbrella/RainCoat stay protected from Irritating Wetness.☔☔😉😉

## Why Rain Alert Application?

Knowing it is going rain in the next 12 hours, You can do so many things.

such as:

Flexing your Friends that you have predicted the Weather Correctly.😉😁

You can take your Umbrella/RainCoat and stay protected from Irritating Wetness.☔☔😉😉.

## Contributing

Contributions are always welcome!

## Feedback

If you have any feedback, please reach out to us.

LinkedIn-[@kavinsanthoshg](https://www.linkedin.com/in/kavinsanthoshg/)

Twitter-[@kavinsanthoshG](https://twitter.com/kavinsanthoshG)

## Badges

![GPLv3 License](https://img.shields.io/badge/License-GNU%20GPL-blue)

## Authors

- [@kavinsanthoshG](https://github.com/kavinsanthoshG)
