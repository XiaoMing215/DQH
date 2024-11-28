import pyautogui
import time
import random

def move_click(x,y,duration,sleep):
    pyautogui.moveTo(x,y, duration)
    pyautogui.click()
    time.sleep(sleep)

location_list=[[1508,638],[1622,624],[1731,624],[1705,768],[1622,741],[1504,762],[1280,733],[1260,846],[1483,833],[1216, 628]]
number=0
find=0
for j in range(0,1):
    for i in range(0,3*len(location_list)):
        x=random.choice(location_list)
        if pyautogui.pixel(x[0],x[1])!=(198, 198, 198):#不是灰的
            find=1
            move_click(x[0],x[1],0.25,0.1)#依次找寻场子
            break
# for j in range(0,1):
#     for i in location_list:
#         if pyautogui.pixel(i[0],i[1])!=(198, 198, 198):#不是灰的
#             find=1
#             move_click(i[0],i[1],0.25,0.1)#依次找寻场子
#             break
if find==0:
    # exit(-3)
    print("no more changzi. time for you to operate.")
    time.sleep(13)
    # continue

if pyautogui.pixel(1600,1320)==(192, 55, 93):
    move_click(1600,1320,0.05,0)#确定

time.sleep(2)    #间隔一段时间
pyautogui.moveTo(1413, 1303, duration=0.05)
pyautogui.scroll(-400)

