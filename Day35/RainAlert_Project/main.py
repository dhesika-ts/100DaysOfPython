import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = [YOUR_API]
account_sid = [YOUR_AUTH_SID]
auth_token = [YOUR_AUTH_TOKEN]
My_Number = [YOUR _MOB_NO]

weather_params = {
    "lat": 11.016010,
    "lon": 76.970306,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()


def will_rain(weather):
    for time in weather:
        condition_code = int(time["weather"][0]["id"])
        if condition_code < 700:
            return True
    return False


weather_data = response.json()
weather_slice = weather_data['list'][:5]

if will_rain(weather_slice):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's Gonna Rain today. Remember to bring an ☔",
        from_='+13345813027',
        to=My_Number
    )

    print(message.status)
