import tkinter as tk
import pyautogui
import random
import time
import threading
import keyboard

# Global variables
bot_running = False
bot_thread = None
monitor_thread = None
reapply_timer = 30  # default wait time after apply clicks (seconds)
accept_img_path = r"C:\Users\alanw\Desktop\Class-2-\Automation tools\Warcraft\Accept button.png"

def update_timer():
    global reapply_timer
    try:
        reapply_timer = float(timer_entry.get())
    except ValueError:
        pass

def update_status(text):
    status_label.config(text=text)

def stop_bot():
    global bot_running
    bot_running = False
    update_status("Stopped")

def monitor_accept_button():
    # Define region using top left (1053,421) and bottom right (1485,492)
    region = (1053, 421, 1485 - 1053, 492 - 421)
    while bot_running:
        try:
            found = pyautogui.locateOnScreen(accept_img_path, region=region, confidence=0.5)
            if found:
                time.sleep(1)
                center = pyautogui.center(found)
                pyautogui.click(center)
                stop_bot()
                break
        except Exception:
            pass
        time.sleep(3)

def bot_loop():
    global bot_running
    while bot_running:
        # Click refresh button and wait 3 seconds (split into 1-sec intervals)
        pyautogui.click(1435, 102)
        for _ in range(3):
            if not bot_running:
                break
            time.sleep(1)
        if not bot_running:
            break

        # Click apply regions in a random order with 1-second delays
        apply_coords = [
            (1300, 153), (1300, 206), (1300, 259), (1300, 313),
            (1300, 367), (1300, 417), (1300, 472), (1300, 524),
            (1300, 581), (1300, 625)
        ]
        random.shuffle(apply_coords)
        for coord in apply_coords:
            if not bot_running:
                break
            pyautogui.click(*coord)
            time.sleep(1)
        if not bot_running:
            break

        # Break up the reapply wait time into 1-second intervals
        for _ in range(int(reapply_timer)):
            if not bot_running:
                break
            time.sleep(1)
        if not bot_running:
            break

        # Click X locations starting from the bottom upward with 1-second delays
        x_coords = [
            (1420, 153), (1420, 206), (1420, 259),
            (1420, 313), (1420, 367), (1420, 625)
        ]
        for coord in sorted(x_coords, key=lambda c: c[1], reverse=True):
            if not bot_running:
                break
            pyautogui.click(*coord)
            time.sleep(1)
        if not bot_running:
            break

        for _ in range(2):
            if not bot_running:
                break
            time.sleep(1)
    update_status("Stopped")

def toggle_bot():
    global bot_running, bot_thread, monitor_thread
    if bot_running:
        stop_bot()
    else:
        bot_running = True
        update_status("Running")
        bot_thread = threading.Thread(target=bot_loop, daemon=True)
        bot_thread.start()
        monitor_thread = threading.Thread(target=monitor_accept_button, daemon=True)
        monitor_thread.start()

# TKinter GUI setup
root = tk.Tk()
root.title("M+ Apply Bot")
root.geometry("350x200")

status_label = tk.Label(root, text="Stopped", font=("Arial", 14))
status_label.pack(pady=10)

timer_frame = tk.Frame(root)
timer_frame.pack(pady=5)
tk.Label(timer_frame, text="Reapply Timer (sec):").pack(side="left")
timer_entry = tk.Entry(timer_frame, width=5)
timer_entry.insert(0, str(reapply_timer))
timer_entry.pack(side="left", padx=5)
tk.Button(timer_frame, text="Update", command=update_timer).pack(side="left")

tk.Label(root, text="Press '#' to toggle bot", font=("Arial", 10)).pack(pady=5)

keyboard.add_hotkey('#', toggle_bot)

root.mainloop()
