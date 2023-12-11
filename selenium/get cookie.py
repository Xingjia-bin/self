import json
import ddddocr
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions
option = EdgeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
# option.add_argument('--headless')
driver = webdriver.Edge(options=option)
driver.set_window_size(1024, 600)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})
def cookies():
    cookie=driver.get_cookies()
    cookie = json.dumps(cookie)
    with open('tianyan.json', 'w') as f:
        f.write(cookie)
if __name__ =='__main__':
    driver.get('https://www.tianyancha.com/')
    time.sleep(60)
    cookies()
