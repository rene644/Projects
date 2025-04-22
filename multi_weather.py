import aiohttp
import asyncio
import os
import json
from dotenv import load_dotenv
from tabulate import tabulate

# ✅ Load Environment Variables
dotenv_path = "C:/Users/renem/OneDrive/Documentos/Python with AI/python_projects/python_projects/weather_projects/.env"
if os.path.exists(dotenv_path):
    print(f"✅ Found .env file at: {dotenv_path}")
    load_dotenv(dotenv_path)
else:
    print("❌ ERROR: .env file not found!")

api_key = os.getenv("API_KEY")
if not api_key:
    print("❌ ERROR: API Key is missing! Check .env formatting.")
else:
    print(f"✅ API Key loaded successfully: {api_key}")

# 🌍 API Configurations
base_url = "http://api.openweathermap.org/data/2.5/weather"
units = "metric"
FAVORITE_CITIES_FILE = "favorite_cities.txt"

def save_favorite_cities(cities):
    """Saves cities correctly in plain text format."""
    with open(FAVORITE_CITIES_FILE, "w") as f:
        f.write("\n".join(cities))  # ✅ Saves each city on a new line
    print(f"✅ Cities saved correctly!")

# 📁 Load Favorite Cities (User Prompt If Missing)
def load_favorite_cities():
    """Loads favorite cities correctly as individual items."""
    if not os.path.exists(FAVORITE_CITIES_FILE) or os.path.getsize(FAVORITE_CITIES_FILE) == 0:
        print("❌ No favorite cities found! Let's add some.")
        cities = input("Enter cities separated by commas: ").split(",")
        cities = [city.strip() for city in cities if city.strip()]
        save_favorite_cities(cities)  # ✅ Save cities properly
        return cities

    try:
        with open(FAVORITE_CITIES_FILE, "r") as f:
            cities = f.read().strip().split("\n")  # ✅ Reads each city separately
            print(f"✅ Loaded Cities (Fixed Format): {cities}")  
            return cities if cities else []
    except Exception as e:
        print(f"❌ Unexpected error while loading favorite cities: {e}")
        return []

# 🌦 Fetch Weather Data
async def fetch_weather(session, city):
    """Fetches weather data asynchronously for one city at a time."""
    city = city.strip()
    print(f"🔍 Requesting weather data for: {city}")
    
    params = {"appid": api_key, "q": city, "units": "metric"}

    try:
        async with session.get(base_url, params=params) as response:
            print(f"🔄 API Response Status for {city}: {response.status}")

            if response.status == 404:
                print(f"❌ City not found: {city}")
                return {"name": city, "temp": "N/A", "condition": "N/A", "humidity": "N/A"}  # ✅ Handle missing data

            elif response.status != 200:
                print(f"❌ API Error {response.status}: {await response.text()}")
                return {"name": city, "temp": "N/A", "condition": "N/A", "humidity": "N/A"}  # ✅ Handle API errors

            data = await response.json()
            print(f"✅ Received API Data for {city}: {data}")

            # ✅ Ensure 'temp', 'weather', and 'humidity' exist before accessing them
            return {
                "name": city,
                "temp": data["main"]["temp"] if "main" in data and "temp" in data["main"] else "N/A",
                "condition": data["weather"][0]["description"] if "weather" in data and data["weather"] else "N/A",
                "humidity": data["main"]["humidity"] if "main" in data and "humidity" in data["main"] else "N/A"
            }
    except Exception as e:
        print(f"❌ Error fetching weather data for {city}: {e}")
        return {"name": city, "temp": "N/A", "condition": "N/A", "humidity": "N/A"}  # ✅ Handle unexpected errors

# 🚀 Run Asynchronous Weather Fetching
async def main():
    cities = load_favorite_cities()  # ✅ Load cities correctly
    print(f"🌍 Cities to check weather for: {cities}")  

    if not cities:
        print("❌ No cities found! Add them to 'favorite_cities.txt'.")
        return

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city) for city in cities]  # ✅ Process one city at a time
        results = await asyncio.gather(*tasks)

        # Display results in a structured table
        table_data = []
        for data in results:
            if data:
                table_data.append([data["name"], f"{data['temp']}°C", data["condition"], f"{data['humidity']}%"])
            else:
                table_data.append(["❌ No Data", "❌ No Data", "❌ No Data", "❌ No Data"])

        print(tabulate(table_data, headers=["City", "Temperature", "Condition", "Humidity"], tablefmt="grid"))

# ✅ Run Script
if __name__ == "__main__":
    asyncio.run(main())
