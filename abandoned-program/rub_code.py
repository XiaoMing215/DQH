import pyautogui
import time
#用于再一次抢场地
pyautogui.moveTo(1413, 1303, duration=0.05)
pyautogui.scroll(-400)
#疯狂点击支付(两次点击之间间隔时间待定)
cnt=0
deltat=0.01
while cnt<90000:
    pyautogui.moveTo(1600, 1550, duration=deltat)
    pyautogui.click()#抢
    cnt+=1
