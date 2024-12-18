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

# Convert latitude and longitude to 3D coordinates
def lat_lon_to_xyz(lat, lon, radius=3185):  # Halved Earth's radius (half of 6371 km)
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    x = radius * np.cos(lat_rad) * np.cos(lon_rad)
    y = radius * np.cos(lat_rad) * np.sin(lon_rad)
    z = radius * np.sin(lat_rad)
    return x, y, z

# Data storage
x_coords = []
y_coords = []
z_coords = []

def update(frame):
    """Fetch the ISS location, update data, and refresh the 3D graph."""
    latitude, longitude = get_iss_location()
    if latitude is not None and longitude is not None:
        x, y, z = lat_lon_to_xyz(latitude, longitude)
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)
        
        # Limit the length of data to avoid performance issues
        if len(x_coords) > 100:
            x_coords.pop(0)
            y_coords.pop(0)
            z_coords.pop(0)
        
        # Clear and update the 3D plot
        ax.clear()
        
        # Plot the Earth (scaled sphere)
        u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
        earth_x = 3185 * np.cos(u) * np.sin(v)  # Adjusted radius for Earth
        earth_y = 3185 * np.sin(u) * np.sin(v)
        earth_z = 3185 * np.cos(v)
        ax.plot_surface(earth_x, earth_y, earth_z, color="blue", alpha=0.2, edgecolor="k")  # 20% transparency
        
        # Plot the ISS path
        ax.plot3D(x_coords, y_coords, z_coords, color="orange", label="ISS Path", alpha=0.7)  # Slight transparency
        ax.scatter(x, y, z, color="red", label="ISS Current Position", alpha=1)  # Fully opaque
        
        ax.set_title("Live ISS Location in 3D Space")
        ax.set_xlabel("X (km)")
        ax.set_ylabel("Y (km)")
        ax.set_zlabel("Z (km)")
        ax.legend()
        ax.grid()

# Setup the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = FuncAnimation(fig, update, interval=5000)  # Update every 15 seconds

# Start the live graph
plt.show()
