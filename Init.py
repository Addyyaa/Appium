from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '13',
        'deviceName': 'Redmi Note 10 Pro',
        'appPackage': 'com.ost.pintura',
        'appActivity': 'io.dcloud.PandoraEntry',
        'automationName': 'UiAutomator2',  # 修正这里的键名
    }
    options = UiAutomator2Options()
    options.load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    driver.implicitly_wait(10)
    return driver
