import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
api_key = os.environ.get("OWM_API_KEY")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": "36.8529",   # ← Virginia Beach 🏖️
    "lon": "-75.9780",  # ← Virginia Beach
    "appid": api_key,
    "cnt": 4,
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:  # ← outside loop ✅
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Rain Alert! ☔\n\nBring an umbrella today!"
        )
        print("Rain alert sent!")
else:
    print("No rain expected today! ☀️")