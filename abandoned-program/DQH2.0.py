#实现基于照片识别的抢选
#目标：发送给任何一个用户都可以帮助其自动下载所需的包
#途径：txt+循环 存储图片的名字
#通过参数调整其模式：循环至某条件，单击&点击n次，滚轮
#通过try排除某些加载异常的情况
import pyautogui
import time
cilck=1
repeat=2
scroll=3 #只支持划到最底部！！！
transform={"click":1,"repeat":2,"scroll":3}

def ReadOperate():
    operate=open(r"D:\Users\ZYM\Desktop\DQH2.0\operate.txt")
    OpList=operate.readlines()
    # print(OpList)
    Opnumbers=list(map(lambda i:transform[i.strip('\n')],OpList))
    return (Opnumbers)

ReadOperate()

def MouseOperate(location,mode,sleep=1,duration=0.1):
    global cilck,repeat,scroll
    #click=1 repeat=2 scroll=3
    x,y=location
    if mode==cilck:
        print("cilck")
        pyautogui.moveTo(x,y,duration)
        pyautogui.click()
        time.sleep(sleep)
    elif mode==repeat:
        print("repeat")
        cnt=0
        deltat=0.06
        while cnt<500:
            pyautogui.moveTo(x,y, duration)
            pyautogui.click()#抢
            cnt+=1
    elif mode==scroll:
        pyautogui.scroll(-800)
        
# picture="D:\\Users\\ZYM\\Desktop\\DQH2.0\\XCX.png"
def FindLocation(picture):
    location=None
    cnt=0
    while location==None and cnt<4:
        location=pyautogui.locateCenterOnScreen(picture)
        print(location)
        cnt+=1
    return location

def main():
    file=open(r"D:\Users\ZYM\Desktop\DQH2.0\picture.txt")
    print(file)
    lines=file.readlines()
    OpnumList=ReadOperate()
    # print(lines)
    PicList=list(map(lambda i:i.strip('\n'),lines))
    All_List=list(zip(PicList,OpnumList))
    # print(All_List)
    for line in All_List:
        picture=line[0].strip('\n')
        print(picture)
        location=FindLocation(picture)
        print(location)
        if location!=None:
            MouseOperate(location,line[1])
        
main()

