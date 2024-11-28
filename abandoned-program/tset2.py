import time
import pyautogui
for i in range(0,30):
    currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置
    print(currentMouseX, currentMouseY)
    color = pyautogui.pixel(currentMouseX, currentMouseY) 
    print(color)
    time.sleep(1.5)


