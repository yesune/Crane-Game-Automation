import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f'Mouse coordinates: {x}, {y}')
    time.sleep(1)
