# import requests
# import time

# def get_iss_location():
#     """Fetches the current location of the ISS from the API and returns latitude and longitude."""
#     url = "http://api.open-notify.org/iss-now.json"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise HTTPError for bad responses
#         data = response.json()
#         if data['message'] == 'success':
#             position = data['iss_position']
#             return float(position['latitude']), float(position['longitude'])
#         else:
#             print("Error in API response.")
#     except requests.RequestException as e:
#         print(f"Error fetching ISS location: {e}")
#     return None, None

# def main():
#     """Fetches and prints the ISS location every 15 seconds."""
#     print("Fetching ISS location every 15 seconds. Press Ctrl+C to stop.")
#     try:
#         while True:
#             latitude, longitude = get_iss_location()
#             if latitude is not None and longitude is not None:
#                 print(f"Current ISS Location: Latitude: {latitude}, Longitude: {longitude}")
#             else:
#                 print("Failed to retrieve ISS location.")
#             time.sleep(15)  # Wait for 15 seconds before fetching again
#     except KeyboardInterrupt:
#         print("\nProgram terminated by user.")

# if __name__ == "__main__":
#     main()




########################################################################################################################


import requests
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def get_iss_location():
    """Fetches the current location of the ISS from the API and returns latitude and longitude."""
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['message'] == 'success':
            position = data['iss_position']
            return float(position['latitude']), float(position['longitude'])
    except requests.RequestException as e:
        print(f"Error fetching ISS location: {e}")
    return None, None

# Data storage
latitudes = []
longitudes = []

def update(frame):
    """Fetch the ISS location, update data, and refresh the graph."""
    latitude, longitude = get_iss_location()
    if latitude is not None and longitude is not None:
        latitudes.append(latitude)
        longitudes.append(longitude)
        
        # Limit the length of data to avoid performance issues
        if len(latitudes) > 100:
            latitudes.pop(0)
            longitudes.pop(0)
        
        # Clear and update the plot
        ax.clear()
        ax.scatter(longitudes, latitudes, color="blue", label="ISS Position")
        ax.plot(longitudes, latitudes, color="orange", linestyle="--", label="Path")
        
        # Line of best fit
        if len(longitudes) > 1:
            coefficients = np.polyfit(longitudes, latitudes, 1)
            best_fit_line = np.poly1d(coefficients)
            ax.plot(longitudes, best_fit_line(longitudes), color="red", label="Best Fit Line")
        
        ax.set_title("Live ISS Location")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.legend()
        ax.grid()

# Setup the plot
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=5000)  # Update every 15 seconds

# Start the live graph
plt.show()
