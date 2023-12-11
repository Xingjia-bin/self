import json
import time
import requests
from lxml import html  # 把lxml是解析xml语言的库
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()

driver.get('http://tjxx.lnu.edu.cn/inputExt.asp')
cookies=driver.get_cookies()
print(cookies)
'''
element = driver.find_element(By.ID, 'kw')
element.send_keys('美女')
element.submit()
'''
elements = driver.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[1]/div[2]/input')
elements.send_keys('20201402106')
elements = driver.find_element(By.XPATH, '//*[@id="sub_form"]/div[1]/div[2]/div[2]/input')
elements.send_keys('Xingjiabin.2002')
elements = driver.find_element(By.XPATH, '//*[@id="sub_form"]/div[1]/div[3]/div[2]/input')
x=input('yzm')
elements.send_keys(x)
elements = driver.find_element(By.XPATH, '//*[@id="formSubmitBtn"]')
elements.click()
time.sleep(4)
cookies=driver.get_cookies()
jsonCookies = json.dumps(cookies)
with open('rb.json', 'w') as f:
      f.write(jsonCookies)
print(cookies)
print(jsonCookies)
'''for i in range(10):
    elements = driver.find_element(By.XPATH, '//*[@id="checkimg"]').click()
    time.sleep(0.5)'''
headers={

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'Cookie': 'ASPSESSIONIDSSATSDTS=HHOMIBIBFKNABDAFAOGNEMIO'
        }

'''to=requests.get('http://tjxx.lnu.edu.cn/inc/checkcode.asp',headers=headers)

with open('checkcode.dib','wb') as f:
    f.write(to.content)
'''

time.sleep(5)
driver.quit()
