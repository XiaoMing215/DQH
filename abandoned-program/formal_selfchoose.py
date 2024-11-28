import pyautogui
import time
import pyperclip
import xlrd
import random

lOrR='left'
clickTimes=1
file = 'cmd.xls'
wb = xlrd.open_workbook("D:\\mycode\\VScode\\python\\program\\"+file)
sheet1 = wb.sheet_by_index(0)
print(type(sheet1))
print(wb.sheet_names())  
wrong=0
# judge=1
def move_click(x,y,duration,sleep):
    pyautogui.moveTo(x,y, duration)
    pyautogui.click()
    time.sleep(sleep)
####删除了机器选场地的功能

i=1
left=0
top=1000
width=1000
height=700#限制搜索范围在左下角
img = sheet1.row(i)[1].value
print(img)
location=pyautogui.locateCenterOnScreen("D:\\mycode\\VScode\\python\\program\\"+img,region=(left, top, width, height)
)
print(location)
if location!=None:
    pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
else:
    print("wrong")
time.sleep(2)

i=2

top=0
left=0
width=1100
height=800
img = sheet1.row(i)[1].value
print(img)#搜索小程序的图片
location=pyautogui.locateCenterOnScreen("D:\\mycode\\VScode\\python\\program\\"+img,region=(left, top, width, height))
print(location)
if location!=None:
    pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
else:
    print("wrong")
    wrong=1
#及时止损
if wrong==1:
    exit(-1)  

time.sleep(3)
move_click(1735,585,0.05,2)
#按到叉

pyautogui.moveTo(1400, 1300, duration=0.25)
pyautogui.scroll(-800)#滑动使其达到底端

move_click(1350,1350,0.25,2)
#羽毛球

move_click(1733,630,0.05,0)
#去预约

move_click(1454,829,0.05,0)
#校内人员

color = pyautogui.pixel(1209, 406)
cnt=0
color = pyautogui.pixel(1209, 406)
cnt=0
while 1:
    color = pyautogui.pixel(1209, 406)
    move_click(1209,406,0.05,0.5)#第二天
    #多次点击 防止人太多卡顿
    cnt+=1
    if color==(177, 6, 145):
        break
    if cnt==7:
        move_click(1075,200,0.05,0.5)#点击退出
        move_click(1733,630,0.05,0)#去预约
        move_click(1454,830,0.05,0)#校内人员
        cnt=0
#点击十次未果 就退出然后冲进


color_before=pyautogui.pixel(1174,810)#确定选择的框跳了出来
while color_before!=(216,147,167):
    time.sleep(1)
    color_before=pyautogui.pixel(1174,810)
    print("wait")
color0 = pyautogui.pixel(1660, 746)
color1 = pyautogui.pixel(1200, 900)
color2 = pyautogui.pixel(1400, 900)
cnt=0

time.sleep(2)

#颜色不是红色就一直点击
# if judge==1:
#     print("wait over")
#     move_click(1660,746,0.25,0)#7-8的场
#     move_click(1200,900,0.25,1)#8-9的场
#     color1 = pyautogui.pixel(1200, 900)
#     color0 = pyautogui.pixel(1660, 746)
# elif judge==2:
#     print("wait over")
#     move_click(1200,900,0.25,0)#8-9的场
#     move_click(1400,900,0.25,1)#9-10的场
#     color1 = pyautogui.pixel(1200, 900)
#     color2 = pyautogui.pixel(1400, 900)


color3 = pyautogui.pixel(1650, 1500)

if color3!=(177,6,54):#不知为何确定按钮附近不是红色（出错）
    exit(-2)

while 1:#找场子的循环
    # time.sleep(0.5)
    # move_click(1650,1550,0.25,0)#点一下查询
    # move_click(1650,1550,0.25,0)#点一下查询
        
    while pyautogui.pixel(1604,464)!=(255, 255, 255):
        time.sleep(0.5)#等待场子的出现
        print("wait for changzi")

    #识5别:点击第一个"人数未满"的场地
    #目前采用不要1号场的list
    location_list=[[1622,624],[1731,624],[1705,768],[1622,741],[1504,762],[1280,733],[1260,846],[1483,833],[1216, 628]]
    # location_list=[[1508,638],[1622,624],[1731,624],[1705,768],[1622,741],[1504,762],[1280,733],[1260,846],[1483,833],[1216, 628]]
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
        continue

    if pyautogui.pixel(1600,1320)==(192, 55, 93):
        move_click(1600,1320,0.05,0)#确定

    time.sleep(2)    #间隔一段时间
    pyautogui.moveTo(1413, 1303, duration=0.05)
    pyautogui.scroll(-400)
    #疯狂点击支付(两次点击之间间隔时间待定)
    cnt=0
    deltat=0.02
    while cnt<250:

        pyautogui.moveTo(1600, 1550, duration=deltat)
        pyautogui.click()#抢
        cnt+=1
    #持续一定时长（半分钟）
    #(超过一定时长 直接退出 再找一个人数未满的场)
    move_click(1075,200,0.05,0.5)#点击退出
