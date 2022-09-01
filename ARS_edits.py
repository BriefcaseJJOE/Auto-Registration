'''
1. download excel file, put in same folder as this script
2. put txt file titled 'labcode.txt' with starting lab code (no spaces) in same folder with this script

'''



import sys
import os
import pandas as pd
import pyautogui as pag

if __name__ == '__main__':
    # read downloaded file
    excel_file = ""
    labcode_file = ''
    for item in  os.listdir():
        if "xlsx" in item:
            excel_file = item
        elif 'labcode' in item:
            labcode_file = item
    
    df = pd.read_excel(excel_file, skiprows=7)
    df = df.sort_values('Unit No')

    ic_nums = df['Identification Number *'].values.tolist()



    # read initial lab code
    with open(labcode_file) as f:
        starting_labcode = f.read()
    


    # generate [(IC, labcode), (IC, labcode), ...]
    print(starting_labcode)
    
    labcode_lis = []

    for i in range(len(ic_nums)):
       

        index = str(int(starting_labcode[3:]) + 1)
        len_index = len(index)
        labcode_lis.append(starting_labcode[:-len_index] + str(index))
        starting_labcode = starting_labcode[:-len_index] + str(index)
        
    #print(labcode_lis)
    data = []
    for i in range(len(ic_nums)):
        
        sub_data = []
        sub_data.append(ic_nums[i])
        sub_data.append(labcode_lis[i])
        data.append(sub_data)6
        sub_data = []
        
        # print(ic_nums[i])
        # print(labcode_lis[i])


    print(data)

    






    # loop and enter data
    pass



    sys.exit(0)












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


# read Identification Numbers column off 








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



