import pyautogui
import keyboard
import time

# Define pixel location and colors
pixel_x, pixel_y = 961, 773 # Coordinates of the pixel to monitor
color_a = (216, 74, 226)  # RGB value for color A
color_b = (121, 21, 148)  # RGB value for color B
print("Monitoring pixel...")
try:
    while True:
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
        time.sleep(.5)

        # Stop condition
        if keyboard.is_pressed('#'):
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("Stopped by user.")
#