# Keylogger Project

## Overview
This repository contains a Python-based keylogger script (`keylogger.py`) designed for educational purposes. The script uses the `pynput`, `requests`, and `pywin32` libraries to capture keystrokes, identify the active application, and send the data to a Discord webhook.

## Features
- Captures keystrokes in real-time.
- Identifies the active window (e.g., browser or application).
- Sends logged data to a Discord channel every 10 seconds or on pressing Enter.
- Stops when the Esc key is pressed.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required dependencies:
   ```bash
   pip install pynput requests pywin32


## Download
To get started with this keylogger script, download the repository or the individual file:
- Clone the repository using Git:
  ```bash
  git clone https://github.com/GhostYasas/keylogger.git

## Run
Ensure Python 3.x is installed on your system. Check with:
      
      python --version
Install the required dependencies:
     
     pip install pynput requests pywin32
Navigate to the folder containing keylogger.py:

     python keylogger.py
## Usage
The script will start logging keystrokes and send them to the configured Discord webhook.
Data is sent every 10 seconds or immediately when you press the Enter key.
The active application (e.g., browser or text editor) is included with the logged text.
Press Esc to stop the script and cancel the timer.
Update the webhook_url in keylogger.py with your Discord webhook URL to receive logs.

## Disclaimer
This script is provided for educational purposes only. Unauthorized use to monitor or record keystrokes on someone else's device without their explicit, informed consent is illegal and unethical. The creator and contributors are not responsible for any misuse, damage, or legal consequences resulting from the use of this code. Use this script responsibly and only on devices you own or have permission to monitor.







