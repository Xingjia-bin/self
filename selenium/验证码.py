import ddddocr
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
ocr = ddddocr.DdddOcr()
with open('checkcode.dib', 'rb') as f:
	img_bytes = f.read()
res = ocr.classification(img_bytes)
print(res)
