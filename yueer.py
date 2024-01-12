import base64
import cv2 as cv
from appium import webdriver
import numpy as np
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {
    'platformName': 'Android',
    'platformVersion': '12',
    'automationName': 'UiAutomator2',
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
with open(r"resource/xuanfuqiu.png", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
element = driver.find_element(by=AppiumBy.IMAGE, value=image_base64)
element.click()
print(element)

