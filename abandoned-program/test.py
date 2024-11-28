import pyautogui
import time
import pyperclip
import xlrd
lOrR='left'
clickTimes=1
file = 'cmd.xls'
wb = xlrd.open_workbook("D:\\mycode\\VScode\\pytest\\program\\"+file)
sheet1 = wb.sheet_by_index(0)
print(type(sheet1))
print(wb.sheet_names())  



wrong=0


i=1

left=0
top=1000
width=1000
height=700#限制搜索范围在左下角
img = sheet1.row(i)[1].value
print(img)
location=pyautogui.locateCenterOnScreen("D:\\mycode\\VScode\\pytest\\program\\"+img,region=(left, top, width, height)
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
height=800#限制搜索范围在左上角
img = sheet1.row(i)[1].value
print(img)#搜索小程序的图片
location=pyautogui.locateCenterOnScreen("D:\\mycode\\VScode\\pytest\\program\\"+img,region=(left, top, width, height))
print(location)
if location!=None:
    pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
else:
    print("wrong")
    wrong=1
time.sleep(3)
#及时止损
if wrong==1:
    exit(-1)  

pyautogui.moveTo(1735, 577, duration=0.05)
pyautogui.click()
#按到叉
# i=3
# left=1550
# top=400
# width=400
# height=300
# img = sheet1.row(i)[1].value
# print(img)
# location=pyautogui.locateCenterOnScreen("D:\\mycode\\VScode\\pytest\\program\\"+img,region=(left, top, width, height))
# print(location)
# if location!=None:
#     pyautogui.click(location.x+10,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
# else:
#     print("wrong")
time.sleep(2)
# i=4
# left=1550
# top=400
# width=1900
# height=300
# img = sheet1.row(i)[1].value
# print(img)
# location=pyautogui.locateCenterOnScreen("D:\\mycode\\VScode\\pytest\\program\\"+img,region=(left, top, width, height))
# print(location)
# if location!=None:
#     pyautogui.click(location.x+10,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
# else:
#     print("wrong")

pyautogui.moveTo(1413, 1303, duration=0.25)
pyautogui.scroll(-800)#滑动使其达到底端

# i=5
# left=900
# top=1000
# width=700
# height=500
# img = sheet1.row(i)[1].value
# print(img)
# location=pyautogui.locateCenterOnScreen("D:\\mycode\\VScode\\pytest\\program\\"+img,region=(left, top, width, height))
# print(location)
# if location!=None:
#     pyautogui.click(location.x+10,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
# else:
#     print("wrong")
pyautogui.moveTo(1400, 1300, duration=0.25)
pyautogui.click()#羽毛球
time.sleep(3)
# i=6
# left=900
# top=1000
# width=700
# height=500
# img = sheet1.row(i)[1].value
# print(img)
# location=pyautogui.locateCenterOnScreen("D:\\mycode\\VScode\\pytest\\program\\"+img,region=(left, top, width, height))
# print(location)
# if location!=None:
#     pyautogui.click(location.x+10,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
# else:
#     print("wrong")


pyautogui.moveTo(1733, 630, duration=0.05)
pyautogui.click()#去预约

pyautogui.moveTo(1454, 829, duration=0.05)
pyautogui.click()#校内人员

color = pyautogui.pixel(1209, 406)
cnt=0
color = pyautogui.pixel(1209, 406)
cnt=0
while 1:
    color = pyautogui.pixel(1209, 406)
    pyautogui.moveTo(1209, 406, duration=0.05)
    pyautogui.click()#第二天   # 像素的坐标位置
    time.sleep(0.5)#多次点击 防止人太多卡顿
    cnt+=1
    if color==(177, 6, 145):
        break
    if cnt==10:
        pyautogui.moveTo(1075,200, duration=0.05)
        pyautogui.click()#退出
        time.sleep(0.5)
        pyautogui.moveTo(1733, 630, duration=0.05)
        pyautogui.click()#去预约

        pyautogui.moveTo(1454, 829, duration=0.05)
        pyautogui.click()#校内人员
        cnt=0

    

# #8-9的场
# # pyautogui.moveTo(1733, 630, duration=0.25)
# # pyautogui.click()

# pyautogui.moveTo(1163, 870, duration=0.05)
# pyautogui.click()#8-9的场

# pyautogui.moveTo(1421, 870, duration=0.05)
# pyautogui.click()#9-10的场
# #待添加:没有检测到红框的时候/某块区域不是红色的时候就一直点
#已经添加完毕
color1 = pyautogui.pixel(1200, 900)
color2 = pyautogui.pixel(1400, 900)
cnt=0

while color1!=(190,53,91) or color2!=(190,53,91):
    color1 = pyautogui.pixel(1200, 900)
    color2 = pyautogui.pixel(1400, 900)
    pyautogui.moveTo(1200, 900, duration=0.05)
    pyautogui.click()#8-9的场 
    pyautogui.moveTo(1400, 900, duration=0.05)
    pyautogui.click()#9-10的场 
    time.sleep(0.5)#多次点击 防止人太多卡顿

color3 = pyautogui.pixel(1650, 1500)
cnt=0
while color3==(177,6,54):
    color3 = pyautogui.pixel(1650, 1500)
    pyautogui.moveTo(1650, 1550, duration=0.05)
    pyautogui.click()#查询
    cnt+=1
    if cnt>2:
        break

while pyautogui.pixel(1604,464)!=(255, 255, 255):
    time.sleep(0.5)


#识别:点击第一个"人数未满"的场地

location_list=[[1508,638],[1622,624],[1731,624],[1705,768],[1622,741],[1504,762],[1280,733],[1260,846],[1483,833],[1216, 628]]
number=0
for j in range(0,1):
    for i in location_list:
        number+=1
        if pyautogui.pixel(i[0],i[1])!=(198, 198, 198):#不是灰的
            pyautogui.moveTo((i[0],i[1]), duration=0.25)#1
            pyautogui.click()
            time.sleep(0.1)
            # if pyautogui.pixel(i[0],i[1])==(190,53,91):
            break
if pyautogui.pixel(1600,1320)==(192, 55, 93):
    pyautogui.moveTo((1600,1320),duration=0.05)
    pyautogui.click#确定

#间隔一段时间
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