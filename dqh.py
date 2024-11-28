#使用opencv进图像识别

import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import time
import pandas as pd
import random
from datetime import datetime, timedelta


# pictureDict = {}


def calculate_manhattan_distance(point1, point2):
    # 计算两点之间的曼哈顿距离
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def sleeping(sleepTime):#更好显示睡眠时间的函数
    if sleepTime<=1: 
        time.sleep(sleepTime)
        return
    for i in range(sleepTime):
        print(sleepTime-i,end='……')
        time.sleep(1) 
    print("")

class RecognizeStrategy:

    
    def DateRecognize(img):
        #识别当天后一天的日期，格式为mm-dd\
        # 获取明天的日期字符串
        today = datetime.datetime.now()
        tomorrow = today + datetime.timedelta(days=1)
        # 根据界面显示的格式调整，例如 "11月21日 星期二"
        tomorrowStr = tomorrow.strftime("%m-%d")

        

# 屏幕截图
def FindLocations(picture,previousPath='',threshold=0.9,distance=10,retryTimes=2,retryDuration=0.3,recognizeFunc="none"):
    '''
    picture:图片名称
    previousPath:DQH3.0目录前的所有路径。支持绝对路径
    retryTimes表示重试次数
    retryDuration表示每次重试的间隔
    返回找到的坐标位置
    '''
    
    # 截取屏幕
    screenshot_path=previousPath+'./DQH3.0/pictures/screenshot.png'  # 你的截图文件路径
    template_path = previousPath+"./DQH3.0/pictures/{}.png".format(picture)  # 你的模板图像路径
    pyautogui.screenshot().save(screenshot_path)


    # 读取模板并查找
    img = cv2.imread(screenshot_path)
    img_template = cv2.imread(template_path)
    if img is None : 
        print("截图文件读取错误")
        exit(-1)
    if img_template is None:
        print("未读到模板图片。")
        exit(-2)
    if recognizeFunc != 'none':
        print('启用特殊识别')
        #特殊识别采用截图图片作为输入
        return getattr(RecognizeStrategy, recognizeFunc)(img)
    else:
        print('启用图片识别')
        # 调用 matchTemplate 函数进行模板匹配
        result = cv2.matchTemplate(img, img_template, cv2.TM_CCOEFF_NORMED)
        
        threshold = 0.9  # 设置阈值
        distance = 10 #曼哈顿相差10像素内的是同一个图像
        old_matches=[]
        matches = []  # 存储所有匹配的坐标

        loc = np.where(result >= threshold)  # 找到所有匹配的位置
        for pt in zip(*loc[::-1]):  # 遍历所有匹配的位置
            center = (int(pt[0] + img_template.shape[1] // 2),int( pt[1] + img_template.shape[0] // 2))
            # 检查是否与旧的匹配足够近
            close_match_found = False
            for old_center in old_matches:
                if calculate_manhattan_distance(center, old_center) < distance:
                    close_match_found = True
                    break
            if not close_match_found:
                matches.append(center)
                old_matches.append(center)
            
        if len(matches)==0 and retryTimes>0:
            print("未找到匹配{0}的图案。{1}秒后重试。".format(picture,retryDuration))
            sleeping(retryDuration)
            matches=FindLocations(picture,previousPath,retryTimes=retryTimes-1,retryDuration=retryDuration)
        elif retryTimes<=0:
            print("重试次数用完，跳过该步骤".format(picture))
            return None
        else:
            print("找到匹配的图案数量：", len(matches))
            print("匹配的坐标：", matches)
            return matches
        return matches

def readFromPicSetting():

    # 读取Excel文件
    df = pd.read_excel('./DQH3.0/command.xlsx', sheet_name='PicSetting',engine='openpyxl',dtype={'图片名称':str})

    step_params = {}

    # 遍历DataFrame中的每一行
    for index, row in df.iterrows():
        step_name = row.iloc[0]
        params = {}
        # 步骤参数是除了第一个元素之外的所有元素
        for param_name, value in zip(('picture', 'previousPath', 'threshold', 'distance','retryTimes','retryDuration'), row[1:]):
            if pd.notna(value):
                params[param_name] = value
        # 将步骤名称和参数字典添加到字典中
        step_params[step_name] = params
    # print(step_params)
    return step_params

def readFromMouseSetting():

    # 读取Excel文件
    df = pd.read_excel('./DQH3.0/command.xlsx', sheet_name='MouseSetting',engine='openpyxl')

    # 创建一个空字典来存储步骤和参数
    step_params = {}

    for index, row in df.iterrows():
        step_name = row.iloc[0]
        params = {}
        for param_name, value in zip(('lOrR', 'enableScroll', 'ScrollParam','clickTimes','duration','chooseFunc'), row[1:]):
            if pd.notna(value):
                params[param_name] = value
        step_params[step_name] = params
    # print(step_params)
    return step_params

#定义点击时采取的策略函数,使用类承接
class ChooseStrategy:
    def Random(locations):
        return random.choice(locations)
    
    def Left(locations):
        #用于处理选择下一天的情况，总是选择最靠屏幕左边的情况
        return min(locations, key=lambda x:x[0])
    def Wait(locations):
        #获取时间，等到正午才会开始尝试点击
        now = datetime.now()
        print(now)
        target_time = datetime(now.year, now.month, now.day, 12, 0, 0)
        print(target_time)
        # 如果当前时间已经超过了目标时间，则将目标时间设置为明天的同一时间
        if now > target_time:
            return max(locations, key=lambda x:x[1])
        time_to_wait = (target_time - now).total_seconds()
        print('{}之后开抢'.format(time_to_wait))
        # time.sleep(time_to_wait)
        # return max(locations, key=lambda x:x[1])
        return locations[-1]
    
    def Custom(locations):
        #根据个人爱好自定义抢购的场地时间
        #这里我定义的是周四8-9，其余时间5-6 6-7 7-8随机
        #不支持周六周日！！！
        now = datetime.now()
        # 计算明天的日期和时间
        tomorrow = now + timedelta(days=1)
        # 获取明天是星期几，weekday()函数返回的是0-6的整数，其中0是星期一，6是星期日
        weekday = tomorrow.weekday()
        # 0-6代表一-日
        if weekday == 5 or weekday == 6:
            print("明天是周末，别打球了")
            return locations[10]
        elif weekday == 3:
            #识别的情况当中就是按照顺序摆好了场地 0-4对应17：00到21：00
            return locations[3]
        else:
            return locations[random.randint(0,2)]


def clickOrScroll(locations,lOrR='left',enableScroll=False,ScrollParam=-1000,clickTimes=1,duration=0.4,chooseFunc='Random'):
    '''
    location:由图像识别传入
    lOrR:左键还是右键还是不点击
    enableScroll:是否需要滚动
    clickTimes:点击次数
    duration:每次点击之间的时间间隔
    chooseFunc:选择点击位置的函数
    '''
    if locations==None:
        print("未找到匹配图案，跳过该步骤")
        return
    
    #采用ChooseStrategy类中的函数具体化选择的函数，默认为随机选择
    location = getattr(ChooseStrategy, chooseFunc)(locations)
    print(location)

    # 滚动处理：默认滑到底部
    if enableScroll != False:
        pyautogui.moveTo(location[0],location[1])
        time.sleep(duration)
        print("正在滚动")
        pyautogui.scroll(ScrollParam)
    if lOrR=='none':
        print("无需点击。")
        return
    clickTimes = int(clickTimes)
    for i in range(clickTimes):
        pyautogui.click(location[0],location[1],button=lOrR)
        time.sleep(duration)
    print("(最多)已点击{}次".format(clickTimes))
    time.sleep(duration)

#考虑使用元组存储一个操作的find location的参数
# 从excel表格读取
#


# 定义一个列表，用于记录步骤的名称
stepList = []
step_params = readFromPicSetting()
mouse_params = readFromMouseSetting()
# print(step_params,mouse_params)

# 记录所有步骤
for key in step_params:
    stepList.append(key)
print("执行列表：{}".format(stepList))

# stepList.append("点击场地")

for stepName in stepList:
    Cparams = step_params.get(stepName)
    Mparams = mouse_params.get(stepName)
    print('{}正在执行'.format(stepName))
    # print(Cparams,Mparams)
    if Cparams:
        # 确保必须参数存在
        if Cparams['picture'] is not None :#还需要进一步错误处理
            # 使用**操作符将参数字典展开为关键字参数
            locations = FindLocations(**Cparams)
            print(Mparams)
            clickOrScroll(locations, **Mparams)
        else:
            print(f"Missing required parameters for step: {stepName}")
    else:
        print(f"No parameters found for step: {stepName}")
        exit(-1)