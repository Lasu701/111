from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_opt = Options()  # 创建参数设置对象.
# chrome_opt.add_argument('--headless')  # 无界面化.
# chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
# chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 2,
#     }
# }
# chrome_opt.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_opt)

driver.get("https://www.huanqiu.com/")
time.sleep(2)

html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')
link = bs.find("div", {"class": "rTxt"}).find_all("a")

lj=[]
for i in link:
    print(i.get('href'))
    s="https:"+i.get('href')
    lj.append(s)

xw=[]
for i in lj:
    try:
        xwlj=[]
        driver.get(i)
        time.sleep(2)

        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')
        link = bs.find("div", {"class": "m-recommend-con"}).find_all("a")
        for j in link:
            s="https://uav.huanqiu.com"+j.get('href')
            xwlj.append(s)
        xw.append(xwlj)
    except:
        continue

# with open("a.txt","w",encoding="utf-8") as f:
#     for i in xw:
#         for j in i:
#             print(j,file=f)
f=open("download.txt","w")
for i in xw:
    for j in i:
        try:
            driver.get(j)
            time.sleep(2)
            html = driver.page_source
            bs = BeautifulSoup(html, 'html.parser')
            tx = bs.find("div", {"class": "l-con"}).get_text()
            f.write(tx)
            print(tx)
        except:
            continue
f.close()

driver.quit()
