import time
import subprocess
import os

# Function to check for mic clicks
def check_mic_clicks():
    # Use your SDR-RTL command to listen for mic clicks on 120.000 MHz
    # Replace 'sdr_command' with the actual command for your SDR-RTL
    sdr_command = "your_sdr_command_here"
    process = subprocess.Popen(sdr_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate(timeout=5)  # Listen for 5 seconds
    # Check if 5 mic clicks were detected
    if output.count(b'mic_click') >= 5:
        return True
    else:
        return False

# Function to turn on USB port
def turn_on_usb():
    # Use command to turn on USB port
    os.system("your_command_to_turn_on_usb_here")

# Function to turn off USB port
def turn_off_usb():
    # Use command to turn off USB port
    os.system("your_command_to_turn_off_usb_here")

# Main loop
while True:
    if check_mic_clicks():
        turn_on_usb()
        # USB stays on for 35 minutes
        time.sleep(35 * 60)
        turn_off_usb()
    else:
        # Sleep for 1 second before checking again
        time.sleep(1)
