import requests

api_key = "c97b27cd3dac515757d084105fa52421"  # Replace with your actual API key
base_url = "http://api.openweathermap.org/data/2.5/weather"
units = 'metric'

cities = [
    {"name": "Pasadena", "country_code": "US", "state_code": "CA"},
    {"name": "Pasadena", "country_code": "US", "state_code": "TX"}
]

print(f"API Key being used: {api_key}")  # For debugging

for city_data in cities:
    city_name = f"{city_data['name']},{city_data['country_code']}"
    params = {
        'appid': api_key,
        'q': city_name,
        'units': units
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        print(f"\nWeather in {data['name']}, {data['sys']['country']} ({city_data['state_code']}):")
        print(f"  Temperature: {data['main']['temp']} °C")
        print(f"  Description: {data['weather'][0]['description']}")
        print(f"  Humidity: {data['main']['humidity']}%")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for {city_name}: {e}")
    except ValueError as e:
        print(f"Error decoding JSON for {city_name}: {e}")
    except KeyError as e:
        print(f"Error accessing data for {city_name}: {e}")