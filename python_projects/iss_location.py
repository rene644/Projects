import requests

try:
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']

    print(f"Current ISS Latitude: {latitude}")
    print(f"Current ISS Longitude: {longitude}")
    print(f"Timestamp: {timestamp}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching ISS location: {e}")
except ValueError as e:
    print(f"Error decoding JSON: {e}")