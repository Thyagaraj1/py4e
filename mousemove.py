#import pyautogui as pag
#import random
#import time

#while True:
    #x=random.randint(600,700)
    #y=random.randint(200,600)
    #pag.moveTo(x,y,0.5)
    #time.sleep(2)

import pyautogui 
import math

# Set the radius of the circle and the center position
radius = 100
center_x, center_y = pyautogui.size()  # Use the screen size as the center position
center_x //= 2  # integer division
center_y //= 2

# Move the mouse cursor in a circle
for angle in range(0, 360, 10):
    # Calculate the next position on the circle
    x = center_x + int(math.cos(math.radians(angle)) * radius)
    y = center_y + int(math.sin(math.radians(angle)) * radius)

    # Move the mouse cursor to the next position
    pyautogui.moveTo(x, y, duration=0.25)