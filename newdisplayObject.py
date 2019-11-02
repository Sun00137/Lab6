from gfxhat import lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar
import math
import random
import time
import os

def turnBacklight():
    backlight.set_all(255,255,255)
    backlight.show()

def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()

def clearScreen():
    lcd.clear()
    lcd.show()

def displayObject(list, startX, startY):
    if startY < 0 :
        startY = 0
    elif startY+ len(list) > 63 :
        startY = 63 - len(list)

    if startX < 0:
        startX = 0
    elif startX + len(list[0]) > 127 :
        startX = 127 - len(list[0])

    for i in range(0, len(list)):
    for j in range(0, len(list[i])):
        lcd.set_pixel(startX+j,startY+i,list[i][j])
        lcd.show()
    time.sleep(1)




test1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

test2 = [
[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]
test3 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

p = [
[1,1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,1,1,1,0,0],
[1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,1,1,0,0],
[1,1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0,0,0,0,0],
]
y = [
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[0,1,1,1,1,0,0,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,1,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
]
t = [
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0],
]
h = [
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
]
o = [
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
]
n = [
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,1,0,0,0,1,1,1,1],
[1,1,1,1,1,0,0,0,1,1,1,1],
[1,1,1,1,1,1,0,0,1,1,1,1],
[1,1,1,1,1,1,0,0,1,1,1,1],
[1,1,1,1,1,1,1,0,1,1,1,1],
[1,1,1,1,1,1,1,0,1,1,1,1],
[1,1,1,1,0,1,1,1,1,1,1,1],
[1,1,1,1,0,1,1,1,1,1,1,1],
[1,1,1,1,0,0,1,1,1,1,1,1],
[1,1,1,1,0,0,1,1,1,1,1,1],
[1,1,1,1,0,0,0,1,1,1,1,1],
[1,1,1,1,0,0,0,1,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
]
smile = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
[0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
[0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
[0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
[0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

turnBacklight()
xChoice = int(input("Choose the starting point x(0-127):"))
yChoice = int(input("Choose the starting point y(0-63):"))
choice  = int(input("Choose an object number(1-4):"))
if choice == 1:
    displayObject(test1,xChoice,yChoice)
    clearScreen()
elif choice == 2:
    displayObject(test2,xChoice,yChoice)
    clearScreen()
elif choice == 3:
    displayObject(test3,xChoice,yChoice)
    clearScreen()
elif choice == 4:
    print("location inputs not allowed: Sorry :(")
    displayObject(p,0,0)
    displayObject(y,12,0)
    displayObject(t,24,0)
    displayObject(h,36,0)
    displayObject(o,48,0)
    displayObject(n,60,0)
    displayObject(smile,80,0)
    clearScreen()
    clearBacklight()
