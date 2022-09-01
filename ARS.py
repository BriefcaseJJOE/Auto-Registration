import pyautogui
import time

a =pyautogui

count = int(input("number of client:"))
load = time.sleep(7)
#excel = (x = 838, y=1038)

#prin = (x=1220, y=504)

#na = (x=831, y=966)

#srs = (x=781, y=1054)

#done = (x=967, y=734)

time.sleep(2)
def toexcel():
    a.moveTo(x = 838, y=1038)
    a.leftClick()
def tosrs():
    a.moveTo(x=781, y=1054)
    a.leftClick()


for i in range(count):
    #mvoe to excel and copy ic number
    toexcel()
    a.keyDown("down")#START ONE TAB ABOVE IC NUMBER AND ONE LEFT!!!
    a.keyDown("right")
    a.hotkey('ctrl', 'c')
    
    #move to srs and paste ic number
    tosrs()
    time.sleep(1)
    a.hotkey('ctrl', 'v')
    
    #clicking contradiction
    a.moveTo(x=831, y=966)
    a.leftClick()
    load
    a.leftClick()
    time.sleep(1)
    
    #move to labcode
    for i in range(4):
        a.keyDown("tab")
    
    
    #move back to excel and move to lab code tab and copy paste
    toexcel()#excel
    time.sleep(1)
    
    #copy labcode
    a.keyDown("left")
    a.hotkey('ctrl', 'c')
    tosrs()
    time.sleep(1)
    a.hotkey('ctrl', 'v')
    a.keyDown("tab")    
    a.keyDown("enter")
    a.keyDown("enter")
    load
    
    
    #clicking print and selecting number for labels and print
    a.moveTo(x=1220, y=504) #print button
    a.leftClick()
    time.sleep(3)
    for i in range(3):
        a.keyDown("tab")

    a.keyDown("3")
    a.keyDown("enter")
    load
    
    #clicking done
    a.moveTo(x=967, y=734)#done button
    a.leftClick()
    load



