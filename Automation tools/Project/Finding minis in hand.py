import pyautogui
import time

# Define the regions to check (left, top, width, height)
regions = [
    (1049, 1197, 151, 120),  # Slot 1
    (1205, 1197, 127, 114),  # Slot 2
    (1356, 1201, 148, 106),  # Slot 3
    (1511, 1201, 134, 111)   # Slot 4
]

# List of image paths for minions
image_paths = [
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Bandit 1.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\DI miner 2.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Emp 4.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Gryf 2.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Pyro 3.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Ranger 5.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Rat miner 1.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Troll 3.png"
]

# Function to check if any image is found in the regions
def check_images_in_regions(image_paths, regions):
    minis_in_hand = []  # Initialize the list to store the minions found in regions
    
    for i, region in enumerate(regions, 1):
        for image_path in image_paths:
            try:
                # Check if the image is found in the current region
                result = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                if result:
                    minion_name = image_path.split("\\")[-1].replace(".png", "")  # Extract the minion name
                    minis_in_hand.append(minion_name)  # Add the minion name to the list
                    print(f"{minion_name} found in Region {i}!")
                    break  # Exit after first image is found in this region
                else:
                    print(f"{image_path} not found in Region {i}.")
            except Exception as e:
                print(f"Error checking {image_path} in Region {i}: {e}")

    print("Minions in hand:", minis_in_hand)  # Print the list of found minions

# Main function to run the check in a loop every 3 seconds
if __name__ == "__main__":
    while True:
        check_images_in_regions(image_paths, regions)
        time.sleep(3)  # Wait for 3 seconds before checking again
