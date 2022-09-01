import time
from os import waitpid
import pyautogui as pag
from PIL import ImageGrab
from PIL import ImageOps
import keyboard
from ctypes import Array
from numpy import *
#time.sleep(3)
#box = ImageGrab.grab(bbox=(983, 323 ,996, 345))
#image = ImageOps.grayscale(box)
###
#image.show()
#time.sleep(3)
#print(pag.position())
#
#946, 118 ,970, 137
#958, 202 ,959, 203

def Togame():
    pag.moveTo(x=563, y=1060)
    pag.click()
    pag.moveTo(x=912, y=516)
while keyboard.is_pressed("q")==False:

    Togame()

