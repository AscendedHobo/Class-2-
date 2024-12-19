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

def haversine(lat1, lon1, lat2, lon2, radius=6371):
    """
    Calculates the great-circle distance between two points on a sphere using the Haversine formula.
    - lat1, lon1: Latitude and Longitude of the first point in degrees.
    - lat2, lon2: Latitude and Longitude of the second point in degrees.
    - radius: Radius of the Earth in kilometers (default 6371 km).
    """
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return radius * c

# Data storage
x_coords = []
y_coords = []
z_coords = []
latitudes = []
longitudes = []
total_distance = 0  # Total distance traveled in km

def update(frame):
    """Fetch the ISS location, update data, and refresh the graph."""
    global total_distance
    
    latitude, longitude = get_iss_location()
    if latitude is not None and longitude is not None:
        # Calculate 3D coordinates
        latitudes.append(latitude)
        longitudes.append(longitude)
        x, y, z = lat_lon_to_xyz(latitude, longitude)
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)

        # Calculate distance if we have at least two points
        if len(latitudes) > 1:
            distance = haversine(latitudes[-2], longitudes[-2], latitudes[-1], longitudes[-1])
            total_distance += distance
        
        # Clear and update the plot
        ax.clear()
        
        # Plot the ISS path
        ax.plot3D(x_coords, y_coords, z_coords, color="orange", label="ISS Path", alpha=0.7)
        ax.scatter(x, y, z, color="red", label="ISS Current Position", alpha=1)

        # Set title and labels
        ax.set_title("Live ISS Location in 3D Space")
        ax.set_xlabel("X (km)")
        ax.set_ylabel("Y (km)")
        ax.set_zlabel("Z (km)")
        ax.legend()
        ax.grid()

        # Display the total distance at the bottom of the graph
        ax.text2D(0.5, -0.1, f"Total Distance Traveled: {total_distance:.2f} km", 
                  transform=ax.transAxes, ha='center', fontsize=10, color='blue')

def lat_lon_to_xyz(lat, lon, radius=6371):  # Earth's radius in km
    """Converts latitude and longitude to 3D Cartesian coordinates."""
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    x = radius * np.cos(lat_rad) * np.cos(lon_rad)
    y = radius * np.cos(lat_rad) * np.sin(lon_rad)
    z = radius * np.sin(lat_rad)
    return x, y, z

# Setup the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = FuncAnimation(fig, update, interval=15000)  # Update every 15 seconds

# Start the live graph
plt.show()
