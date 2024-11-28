import time
import datetime
from datetime import datetime, timedelta
def Wait():
    #获取时间，等到正午才会开始尝试点击
    now = datetime.now()
    print(now)
    target_time = datetime(now.year, now.month, now.day, 11, 59, 55)
    print(target_time)
    time_to_wait = (target_time - now).total_seconds()
    print('{}之后开抢'.format(time_to_wait))
    time.sleep(time_to_wait)
Wait()
