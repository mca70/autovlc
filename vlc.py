import subprocess
import pygetwindow as gw
import pyautogui
import time

# Specify the path to the VLC executable
vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"  # Update this path to match your VLC installation location

# Launch nine instances of VLC Player
for _ in range(9):
    subprocess.Popen([vlc_path])

# Give some time for VLC to open
time.sleep(5)

# Get all VLC windows
vlc_windows = gw.getWindowsWithTitle('VLC media player')

# Define the grid size
grid_columns = 3
grid_rows = 3

# Get the screen width and height using 2pyautogui
screen_width, screen_height = pyautogui.size()

# Calculate the window width and height based on screen resolution
window_width = screen_width // grid_columns
window_height = screen_height // grid_rows

# Position and resize each VLC window
for i, window in enumerate(vlc_windows):
    if i < grid_columns * grid_rows:
        column = i % grid_columns
        row = i // grid_columns
        x = column * window_width
        y = row * window_height
        window.moveTo(x, y)
        window.resizeTo(window_width, window_height)
