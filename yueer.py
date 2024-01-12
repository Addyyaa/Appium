import base64
from time import sleep

import cv2 as cv
import selenium.common.exceptions
from appium import webdriver
import numpy as np
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import subprocess

"""
安装image插件：appium plugin install images
使用插件：appium --base-path /wd/hub --use-plugins=images
"""
desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12',
        'deviceName': 'Smart VC',
        'automationName': 'UiAutomator2',
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# with open(r"resource/xuanfuqiu.png", "rb") as image_file:
#     image1 = base64.b64encode(image_file.read()).decode("utf-8")
# with open(r"resource/quickbutton.png", "rb") as image_file:
#     image2 = base64.b64encode(image_file.read()).decode("utf-8")
# element1 = driver.find_element(by=AppiumBy.IMAGE, value=image1)
# element1.click()
# element2 = driver.find_element(by=AppiumBy.IMAGE, value=image2)
def wait_find(strategy, element, timeout=10):
    if strategy.upper() == 'XPATH':
        return WebDriverWait(driver, timeout).until(
            ec.visibility_of_element_located((By.XPATH, element))
        )
    elif strategy.upper() == 'ID':
        return WebDriverWait(driver, timeout).until(
            ec.visibility_of_element_located((By.ID, element))
        )
    elif strategy.upper() == 'CLASSNAME':
        return WebDriverWait(driver, timeout).until(
            ec.visibility_of_element_located((By.CLASS_NAME, element))
        )
    elif strategy.upper() == 'NAME':
        return WebDriverWait(driver, timeout).until(
            ec.visibility_of_element_located((By.NAME, element))
        )
    elif strategy.upper() == 'CSS_SELECTOR':
        return WebDriverWait(driver, timeout).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, element))
        )

def run_adb_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
# pc = wait_find("id", "com.yuerin.launcher:id/btn_switch_uvc")
# for i in range(5):
#     element1.click()
#     element2.click()
#     pc.click()
#     driver.press_keycode(4)
current_activity = driver.current_activity
print("当前活动:", current_activity)

current_package = driver.current_package
print("当前应用包名:", current_package)
for i in range(5):
    if current_package == "com.yuerin.setting":
        # 测试HDMI IN
        display = wait_find('xpath',
                            '//android.widget.TextView[@resource-id="com.yuerin.setting:id/name" and @text="显示"]')
        display.click()
        hdmi_in = wait_find('id', 'com.yuerin.setting:id/tv_hdmi_in_label')
        hdmi_in.click()
    elif current_package == "com.yuerin.launcher" and current_activity == ".ui.home.HomeActivity":
        try:
            wait_find("id", "com.yuerin.launcher:id/btn_setting")
            # 测试HDMI IN
            display = wait_find('xpath',
                                '//android.widget.TextView[@resource-id="com.yuerin.setting:id/name" and @text="显示"]')
            display.click()
            hdmi_in = wait_find('id', 'com.yuerin.setting:id/tv_hdmi_in_label')
            hdmi_in.click()
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
            print("未找到设置按钮")
    sleep(10)
    driver.press_keycode(4)
    driver.press_keycode(4)
    run_adb_command("adb logcat > d:hdmi.txt")

