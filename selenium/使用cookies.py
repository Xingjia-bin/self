import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions
option = EdgeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('detach',True)
# option.add_argument('--headless')
driver = webdriver.Edge(options=option)
driver.set_window_size(1024, 600)
driver.get('http://canovel.com')
time.sleep(120)
cookie = driver.get_cookies()
cookie = json.dumps(cookie)
with open('ca.json', 'w') as f:
        f.write(cookie)
# driver.delete_all_cookies()
# with open('rb.json','r')as f:
#       cookie = f.read()
#       cookie = json.loads(cookie)
# for c in cookie:
#       driver.add_cookie(c)
# driver.refresh()
print(driver.get_cookies())
time.sleep(5)
