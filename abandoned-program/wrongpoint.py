import pyautogui
import time
judge=2
def move_click(x,y,duration,sleep):
    pyautogui.moveTo(x,y, duration)
    pyautogui.click()
    time.sleep(sleep)

time.sleep(3)
#颜色不是红色就一直点击
if judge==1:
    move_click(1660,746,0.05,0)#7-8的场
    move_click(1200,900,0.05,1)#8-9的场
    color1 = pyautogui.pixel(1200, 900)
    color0 = pyautogui.pixel(1660, 746)
elif judge==2:
    move_click(1200,900,0.05,0)#8-9的场
    move_click(1400,900,0.05,1)#9-10的场
    color1 = pyautogui.pixel(1200, 900)
    color2 = pyautogui.pixel(1400, 900)


color3 = pyautogui.pixel(1650, 1500)

if color3!=(177,6,54):#不知为何确定按钮附近不是红色（出错）
    exit(-2)

while 1:#找场子的循环
    time.sleep(1)
    move_click(1650,1550,0.25,0)#点一下查询
    move_click(1650,1550,0.25,0)#点一下查询
        
    while pyautogui.pixel(1604,464)!=(255, 255, 255):
        time.sleep(0.5)#等待场子的出现
        print("wait for changzi")

    #识别:点击第一个"人数未满"的场地
    location_list=[[1508,638],[1622,624],[1731,624],[1705,768],[1622,741],[1504,762],[1280,733],[1260,846],[1483,833],[1216, 628]]
    number=0
    find=0
    for j in range(0,1):
        for i in location_list:
            number+=1
            if pyautogui.pixel(i[0],i[1])!=(198, 198, 198):#不是灰的
                find=1
                move_click(i[0],i[1],0.25,0.1)#依次找寻场子
                break
    if find==0:
        exit(-3)

    if pyautogui.pixel(1600,1320)==(192, 55, 93):
        move_click(1600,1320,0.05,0)#确定

    time.sleep(4)    #间隔一段时间
    pyautogui.moveTo(1413, 1303, duration=0.05)
    pyautogui.scroll(-400)
    #疯狂点击支付(两次点击之间间隔时间待定)
    cnt=0
    deltat=0.02
    while cnt<600:
        pyautogui.moveTo(1600, 1550, duration=deltat)
        pyautogui.click()#抢
        cnt+=1
    #持续一定时长（半分钟）
    #(超过一定时长 直接退出 再找一个人数未满的场)
    move_click(1075,200,0.05,0.5)#点击退出
