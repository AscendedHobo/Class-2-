import pyautogui
import threading
import tkinter as tk
from tkinter import messagebox
import time

# Define pixel location and colors
pixel_x, pixel_y = 961, 773  # Coordinates of the pixel to monitor
color_a = (216, 74, 226)     # RGB value for color A
color_b = (121, 21, 148)     # RGB value for color B

# Flag to control monitoring
monitoring = False

# Function to monitor pixel
def monitor_pixel():
    global monitoring
    print("Monitoring started...")
    try:
        while monitoring:
            # Get the current color of the pixel
            current_color = pyautogui.pixel(pixel_x, pixel_y)

            if current_color == color_a:
                pyautogui.press('[')
                print("Color A detected. Pressed Left button.")

            elif current_color == color_b:
                pyautogui.keyDown('shift')
                time.sleep(0.3)
                pyautogui.press('[')
                time.sleep(0.3)
                pyautogui.keyUp('shift')
                time.sleep(0.3)
                print("Color B detected. Pressed Shift + Left button.")

            # Delay to prevent overloading the CPU
            time.sleep(0.5)

    except Exception as e:
        print(f"Error: {e}")

# Start monitoring in a separate thread
def start_monitoring():
    global monitoring
    if not monitoring:
        monitoring = True
        thread = threading.Thread(target=monitor_pixel)
        thread.daemon = True  # Ensure thread exits when main program closes
        thread.start()
    else:
        messagebox.showinfo("Info", "Monitoring is already running.")

# Stop monitoring
def stop_monitoring():
    global monitoring
    if monitoring:
        monitoring = False
        print("Monitoring stopped.")
    else:
        messagebox.showinfo("Info", "Monitoring is not running.")

# Create the GUI window
root = tk.Tk()
root.title("Pixel Monitor")
root.geometry("300x150")

# Create buttons
start_button = tk.Button(root, text="Start Monitoring", command=start_monitoring, width=20, height=2)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Monitoring", command=stop_monitoring, width=20, height=2)
stop_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
