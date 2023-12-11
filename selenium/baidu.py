import json
import ddddocr
import time
#import requests
#from lxml import html
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
    driver.get('https://www.baidu.com/')
    driver.delete_all_cookies()
    with open('bu.json', 'r') as f:
        cookie = f.read()
        cookie = json.loads(cookie)
    for c in cookie:
        driver.add_cookie(c)
    driver.refresh()
    time.sleep(10)
    driver.quit()
def cookies():
    cookie = driver.get_cookies()
    cookie = json.dumps(cookie)
    with open('bu.json', 'w') as f:
        f.write(cookie)

if __name__ == '__main__':
    login()


