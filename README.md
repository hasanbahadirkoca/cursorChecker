# Mouse Cursor Tracker

This Python script monitors the movement of the mouse cursor on the screen and prints an error message if it remains stationary for a certain amount of time. The script uses the `pyautogui`, `requests`, and `time` libraries.

## Requirements

- `pyautogui` module must be installed. To install it, run `pip install pyautogui` in the command line.

## Usage

1. Download the script and save it to your computer.
2. Open a command prompt or terminal window and navigate to the directory where the script is saved.
3. Run the script by entering `python cursor_movement_monitor.py` in the command prompt or terminal window.

## How it Works

The script starts by getting the initial position of the cursor and the start time using the `get_cursor_position` and `time.time` functions, respectively.

The `while` loop runs continuously, getting the current position of the cursor using `get_cursor_position` and calculating the time elapsed since the last cursor movement using the `time.time` function.

If the cursor hasn't moved for the specified amount of time (`SECONDS`), the script prints an error message. Otherwise, the script updates the `last_position` and `start_time` variables and waits for a short period of time before checking the cursor position again.
