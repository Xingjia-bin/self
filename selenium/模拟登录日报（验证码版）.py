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

def ocr(img):
    ocrr = ddddocr.DdddOcr()
    with open(img, 'rb') as f:
        img_bytes = f.read()
    res = ocrr.classification(img_bytes)
    return res


def login():
    driver.get('http://tjxx.lnu.edu.cn/login.asp')
    img = driver.find_element(By.XPATH, '//*[@id="checkimg"]')
    img.screenshot('rb.png')
    elements = driver.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[1]/div[2]/input')
    elements.send_keys('20201402106')
    elements = driver.find_element(By.XPATH, '//*[@id="sub_form"]/div[1]/div[2]/div[2]/input')
    elements.send_keys('Xingjiabin.2002')
    elements = driver.find_element(By.XPATH, '//*[@id="sub_form"]/div[1]/div[3]/div[2]/input')
    elements.send_keys(ocr('rb.png'))
    elements = driver.find_element(By.XPATH, '//*[@id="formSubmitBtn"]')
    elements.click()
    time.sleep(5)
    cookies()
    driver.quit()
def cookies():
    cookie=driver.get_cookies()
    cookie = json.dumps(cookie)
    with open('rb.json', 'w') as f:
        f.write(cookie)

if __name__ == '__main__':
    login()


