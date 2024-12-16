import requests
import time

def get_iss_location():
    """Fetches the current location of the ISS from the API and returns latitude and longitude."""
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        if data['message'] == 'success':
            position = data['iss_position']
            return float(position['latitude']), float(position['longitude'])
        else:
            print("Error in API response.")
    except requests.RequestException as e:
        print(f"Error fetching ISS location: {e}")
    return None, None

def main():
    """Fetches and prints the ISS location every 15 seconds."""
    print("Fetching ISS location every 15 seconds. Press Ctrl+C to stop.")
    try:
        while True:
            latitude, longitude = get_iss_location()
            if latitude is not None and longitude is not None:
                print(f"Current ISS Location: Latitude: {latitude}, Longitude: {longitude}")
            else:
                print("Failed to retrieve ISS location.")
            time.sleep(15)  # Wait for 15 seconds before fetching again
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
