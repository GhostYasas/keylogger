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


