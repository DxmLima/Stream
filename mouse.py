# Use This File for check you XY mouse

import pyautogui
import time

# Adjut the number for a time you need to point your mouse in destined location
time.sleep(3)
mouse = pyautogui.position()  # current mouse x and y

print(mouse)
