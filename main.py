'''

Requirements:

- pip install pyautogui

'''


import pyautogui
import requests
import time

SECONDS = 20  # The number of seconds before the script prints an error message.

def get_cursor_position(): 
    # A function to get the current position of the cursor.
    x, y = pyautogui.position()
    return x, y

if __name__ == "__main__":
    last_position = get_cursor_position()
    start_time = time.time()

    while True:
        current_position = get_cursor_position()

        last_action_time = round(time.time() - start_time, 1)

        print(f"Cursor position: {current_position} - {last_action_time} seconds")

        if current_position == last_position:
            elapsed_time = time.time() - start_time

            if elapsed_time >= SECONDS:
                print(f"Error: Cursor has not moved for {SECONDS} seconds.")
                start_time = time.time()
        else:
            start_time = time.time()

        last_position = current_position
        time.sleep(0.1)
