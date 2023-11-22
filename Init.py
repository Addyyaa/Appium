# Init.py
from appium import webdriver

def get_driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '13',
        'deviceName': 'Redmi Note 10 Pro',
        'appPackage': 'com.ost.pintura',
        'appActivity': 'io.dcloud.PandoraEntry'
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver
