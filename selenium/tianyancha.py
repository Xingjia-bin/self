import json
import ddddocr
import driver as driver
from lxml import etree
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))  #显示等待
option = EdgeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
# option.add_argument('--headless')
driver = webdriver.Edge(options=option)
driver.set_window_size(1024, 600)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})



class tianyancha(object):
    def __init__(self,url,delay=3):
        self.url=url
        self.delay=delay

    def login(self):
        driver.get(self.url)
        time.sleep(3)
        # try:
        #     element = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, '//*[@id="page-container"]/div/div[2]/section/main/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/a/span'))
        #     )
        # finally:
        #     pass


    def get(self):
        response=driver.page_source
        print(response)

    def parse(self,response,xpath):
        tree=etree.HTML(response)
        address=tree.xpath(xpath)
        print(address)

    def find(self,xpath):
        return driver.find_element(By.XPATH,xpath)











if __name__ == '__main__':
    xpath='/html/body/div/div[2]/div/div[2]/section/main/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[6]/div/span[2]/text()[1]'
    address=tianyancha('https://www.tianyancha.com/search?key=%E9%87%91%E8%9E%8D%E7%A7%91%E6%8A%80&sessionNo=1683681603.21696078')
    address.login()
    address.get()
    a=driver.find_element(By.TAG_NAME,'span').
    # a=driver.find_element(By.)
    # print(a.text)

    #
    # text=address.find(xpath)
    # print(text.text)


    # address.parse(address.get(),xpath)


