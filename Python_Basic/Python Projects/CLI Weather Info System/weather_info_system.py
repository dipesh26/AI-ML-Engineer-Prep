import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_Key = os.getenv("OWM_API_KEY")

def get_weather(city, api_key):
    
    if not city.isalpha():
        print("⚠️ Please enter a valid city name (letters only).")
        return
    
    try:
        print("DEBUG - API Key:", api_key)

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()
        # print(data)
        print("\nDEBUG - API Response:")
        print(data)  # 👈 Print full response to see what's going wrong

        if response.status_code != 200 or "main" not in data:
            print(f"❌ API Error: {data.get('message', 'Unknown error')}")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        deg = data["wind"].get("deg", "N/A")
        country = data["sys"]["country"]
        city_name = data["name"]

        print(f"\n📍 Weather Info for {city_name.capitalize()}, {country}:")
        print(f"🌡️ Temperature     : {temp}°C")
        print(f"💧 Humidity        : {humidity}%")
        print(f"🔽 Pressure        : {pressure} hPa")
        print(f"🌥️ Condition       : {weather}")
        print(f"💨 Wind Speed      : {wind_speed} m/s")
        print(f"🧭 Wind Direction  : {deg}°")

    except ValueError as ve:
        print(f"❌ Error: {ve}")
    
    except Exception as e:
        print(f"❌ Something went wrong: {e}")

while True:
    city = str(input("Enter city name (or type 'exit' to quit): ")).strip()
    if city.lower() == "exit":
        print("Thank for Using Us..")
        break

    get_weather(city, API_Key)