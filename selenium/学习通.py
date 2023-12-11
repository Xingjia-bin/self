import json
import ddddocr
import time
#import requests
#from lxml import html  # 把lxml是解析xml语言的库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

option = Options()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
# option.add_argument('--headless')
driver = webdriver.Edge(options=option)
driver.set_window_size(1024, 600)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})

# option.add_argument('--headless')
driver = webdriver.Edge(options=option)



def ocr(img):
    ocrr = ddddocr.DdddOcr()
    with open(img, 'rb') as f:
        img_bytes = f.read()
    res = ocrr.classification(img_bytes)
    return res


def login():
    driver.get('https://passport2.chaoxing.com/login?fid=9332&refer=http://i.mooc.chaoxing.com')
    time.sleep(5)
    elements = driver.find_element(By.XPATH, '//*[@id="phone"]')
    elements.send_keys('13216521138')
    elements = driver.find_element(By.XPATH, '//*[@id="pwd"]')
    elements.send_keys('xxy121233')
    elements = driver.find_element(By.XPATH,'//*[@id="loginBtn"]')
    elements.click()
    time.sleep(500)
def cookies():
    cookie = driver.get_cookies()
    cookie = json.dumps(cookie)
    with open('xxt.json', 'w') as f:
        f.write(cookie)

if __name__ == '__main__':
    login()

