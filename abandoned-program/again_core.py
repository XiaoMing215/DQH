import pyautogui
import time
#用于再一次抢场地
color1 = pyautogui.pixel(1200, 900)
color2 = pyautogui.pixel(1400, 900)
cnt=0

color1 = pyautogui.pixel(1200, 900)
color2 = pyautogui.pixel(1300, 900)
# pyautogui.moveTo(1200, 900, duration=0.05)
# pyautogui.click()#8-9的场 
# pyautogui.moveTo(1400, 900, duration=0.05)
# pyautogui.click()#9-10的场 
# time.sleep(0.5)#多次点击 防止人太多卡顿

# color3 = pyautogui.pixel(1650, 1500)
# cnt=0
# while color3==(177,6,54):
#     color3 = pyautogui.pixel(1650, 1500)
#     pyautogui.moveTo(1650, 1550, duration=0.05)
#     pyautogui.click()#查询
#     cnt+=1
#     if cnt>6:
#         break

# while pyautogui.pixel(1604,464)!=(255, 255, 255):
#     time.sleep(0.5)


# #识别:点击第一个"人数未满"的场地

# location_list=[[1508,638],[1622,624],[1731,624],[1705,768],[1622,741],[1504,762],[1280,733],[1260,846],[1483,833],[1216, 628]]
# number=0
# for j in range(0,1):
#     for i in location_list:
#         number+=1
#         if pyautogui.pixel(i[0],i[1])!=(198, 198, 198):#不是灰的
#             pyautogui.moveTo((i[0],i[1]), duration=0.25)#1
#             pyautogui.click()
#             time.sleep(0.1)
#             # if pyautogui.pixel(i[0],i[1])==(190,53,91):
#             break
# if pyautogui.pixel(1600,1320)==(192, 55, 93):
#     pyautogui.moveTo((1600,1320),duration=0.05)
#     pyautogui.click#确定

# # #间隔一段时间
time.sleep(3)
pyautogui.moveTo(1413, 1303, duration=0.05)
pyautogui.scroll(-400)
#疯狂点击支付(两次点击之间间隔时间待定)
cnt=0
deltat=0.06
while cnt<500:
    pyautogui.moveTo(1600, 1550, duration=deltat)
    pyautogui.click()#抢
    cnt+=1
#持续一定时长
#(检测是否出现待支付 没有出现就继续点击)
#(超过一定时长 直接退出 再找一个人数未满的场)