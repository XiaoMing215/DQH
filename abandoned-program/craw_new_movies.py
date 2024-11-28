##这里直接模拟网页 不用bs 防止加载出错 

from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By  
import mysql.connector  #pip install mysql-connector-python
import re

# 配置数据库连接  
db_config = {  
    'user': 'zym',  
    'password': '123456',  
    'host': 'localhost',  
    'database': 'movies',  
    'raise_on_warnings': True  
}  
  
def extract_info(text):
    # 使用正则表达式匹配导演、上映日期和片长
    director_pattern = r"导演: (.+?)[编]"
    # date_pattern = r"上映日期: (.+?)[(]"
    date_region_pattern = r"上映日期: (.+?)\)" 
    duration_pattern = r"片长: (.+?)分钟"

    # 搜索并提取信息
    director = re.search(director_pattern, text)
    date_region = re.search(date_region_pattern, text)
    # date = re.search(date_pattern, text)
    date = date_region.group(1).split('(')[0] if date_region else '未知'
    region = date_region.group(1).split('(')[1].rstrip(')') if date_region else '未知'
    duration = re.search(duration_pattern, text)

    # 将提取的信息以字典形式返回
    return {
        '导演': director.group(1) if director else '未知',
        '上映日期': date if date else '未知',
        "地区": region if region else '未知',
        '片长': duration.group(1)+"分钟" if duration else '未知'
    }

# 调用函数并打印结果

def insert_data(url):  
    #给予网址，把所有内容插入到数据库
    cursor = cnx.cursor()  
    #找到所有要插入的项
    driver.get(url)  
    driver.implicitly_wait(1)
    all_data=''
    datas=driver.find_elements(By.XPATH,r'//*[@id="info"]/span')
    name=driver.find_element(By.XPATH,r'//*[@id="content"]/h1/span[1]').text.replace('\'','‘').replace('\"','“')#//*[@id="content"]/h1/span[1]
    score=driver.find_element(By.XPATH,r'//*[@id="interest_sectl"]/div[1]/div[2]/strong').text#//*[@id="interest_sectl"]/div[1]/div[2]/strong
    # //*[@id="info"]/span[14] //*[@id="info"]/span[5]
    for data in datas:  
        all_data+=data.text
        all_data+=' '
    data_to_insert=extract_info(all_data)
    print(data_to_insert)
    data_tuple = ', '.join([f"'{value}'" for key,value in data_to_insert.items()])
    insert_sentence="'"+name+"','"+score+"',"+data_tuple    # 检查数据库中是否已存在该条目的查询
    check_query = f"SELECT * FROM tblname WHERE director='{data_to_insert['导演']}' AND releasetime='{data_to_insert['上映日期']}'"
    cursor.execute(check_query)
    existing_row = cursor.fetchone()
    if existing_row:
        existing_score = existing_row[5]

        # 计算新的score与现有score的差异
        score_change =round(float(score) - float(existing_score),1)
        if score_change > 0:  # 如果score_change大于0，说明新评分比现有评分高，将change字段设置为'+1'  
            score_change = '+'+str(score_change)  
        else:  # 如果score_change小于等于0，说明新评分比现有评分低，将change字段设置为'+1'  
            score_change = str(score_change)
        # 更新数据库中的score和change字段
        update_query = """
        UPDATE tblname
        SET score = %s, scorechange = %s,number=number+1
        WHERE director=%s AND releasetime=%s
        """
        cursor.execute(update_query, (score, score_change, data_to_insert['导演'], data_to_insert['上映日期']))
    else:
    # 如果不存在，插入新条目
        print(insert_sentence)
        insert_query = f"INSERT INTO tblname (name,score,director, releasetime,region,duration) VALUES ({insert_sentence})"
        cursor.execute(insert_query)

    # query = f"INSERT INTO tblname (name) VALUES ('{data_to_insert}')"  
    # cursor.execute(query)  



  
# 初始化WebDriver  
driver = webdriver.Chrome()  
  
try:  
    # 打开网页  
    driver.get('https://movie.douban.com/chart')  
      
    # 假设我们获取网页上某个元素的值  
    elements = driver.find_elements(By.XPATH,r'//*[@id="content"]/div/div[1]/div/div/table/tbody/tr/td[2]/div/a')  
                
  
    # 连接到MySQL数据库  
    cnx = mysql.connector.connect(**db_config)  
    cursor = cnx.cursor()  
  
    urls=[]
    for element in elements:  
        name= element.text  
        url=element.get_attribute('href')
        urls.append(url)
    
    for url in urls:
        print(url)
        insert_data(url)
        # 准备SQL语句（这里以插入为例，更新的话需要修改WHERE子句）  
        cnx.commit()  
        print("数据已成功插入数据库")  
      

  
except Exception as e:  
    print(f"发生错误：{e}")  
    if cnx.is_connected():  
        cnx.rollback()  # 如果发生错误，则回滚  
  
finally:  
    # 关闭数据库连接  
    if cnx.is_connected():  
        cursor.close()  
        cnx.close()  
  
    # 关闭WebDriver  
    driver.quit()