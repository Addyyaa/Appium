import re
import selenium.common.exceptions
import Init
import Element
import ElementTips
import Config
import pytest
import logging
from selenium.webdriver.common.by import By
import VersionSelection
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import phonenumbers
import ElementSMS


class TestRegister:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, goto_register_page, info):
        # 通过参数引用 goto_register_page fixture
        app_language, region, elements, tips_element, config = info
        driver = Init.get_driver()
        driver.implicitly_wait(10)
        version = VersionSelection.VersionSelection(driver)
        version.version_selection(region, app_language)
        logger = logging.getLogger(__name__)

        # 在 setup 中调用 goto_register_page
        goto_register_page(driver, elements, app_language, logger)

        yield {
            "driver": driver,
            "logger": logger
        }
        sleep(3)
        driver.quit()

    @pytest.fixture(scope="session", autouse=True)
    def info(self):
        app_language = "Chinese"
        region = "Chinese"
        register_type = 'phone'
        elements = Element.Element_version
        tips_element = ElementTips.register_page_tips
        config = Config.Config
        return app_language, region, elements, tips_element, config

    # 定义为 fixture，并作为参数传递给 setup
    @pytest.fixture(scope="class", autouse=True)
    def goto_register_page(self):
        def _goto_register_page(driver, elements, app_language, logger):
            if app_language == "Chinese":
                try:
                    WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located((By.XPATH, elements.Ch_LoginPage_Register))).click()
                except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                    logger.error("未找到注册按钮")
            elif app_language == 'English':
                try:
                    WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located((By.XPATH, elements.En_LoginPage_Register))).click()
                except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                    logger.error("未找到注册按钮")
            else:
                logger.error("请配置正确的语言")

        return _goto_register_page

    def register_method_switch(self):
        # TODO 需要根据register_type进行切换注册方式
        pass

    # 手机区号根据x、y点击
    def area_code_click(self, driver):
        x = 500
        y = 1090
        touch = TouchAction(driver)
        touch.tap(x=x, y=y).perform()

    def area_code_select(self, driver, elements, app_language, logger, region):
        if region == "Chinese":
            code_text = "中国大陆"
            code_area = elements.Ch_Phone_Register_86
        elif region == "English":
            code_text = "美国"
            code_area = elements.En_Phone_Register_1
        else:
            code_text = None
            code_area = None
            logger.error("请输入国家名称或国家代号")
        if app_language == "English":
            driver.find_element(By.XPATH, elements.En_Phone_Register_AreaCodeList).click()
            sleep(2)
            self.area_code_click(driver)
            logger.info("已点击搜索框")
            # 选择区号
            driver.find_element(By.XPATH, elements.Ch_Phone_Register_AreaCode_Search).send_keys(code_text)
            logger.info("已发送搜索文本")
            driver.hide_keyboard()
            logger.info("已关闭虚拟键盘")
            driver.find_element(By.XPATH, code_area).click()
        elif app_language == "Chinese":
            driver.find_element(By.XPATH, elements.Ch_Phone_Register_AreaCodeList).click()
            sleep(2)
            self.area_code_click(driver)
            logger.info("已点击搜索框")
            # 选择区号
            driver.find_element(By.XPATH, elements.Ch_Phone_Register_AreaCode_Search).send_keys(code_text)
            logger.info("已发送搜索文本")
            driver.hide_keyboard()
            logger.info("已关闭虚拟键盘")
            driver.find_element(By.XPATH, code_area).click()
        else:
            logger.error("请输入正确的语言")
    def test_casse(self, setup, info):
        app_language, region, elements, tips_element, config = info
        driver = setup["driver"]
        logger = setup["logger"]
        self.area_code_select(driver, elements, app_language, logger, region)
