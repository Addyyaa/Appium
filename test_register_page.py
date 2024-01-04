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
import pdb


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
        app_language = "English"
        region = "China"
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
                    driver.press_keycode(4)
                    WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located((By.XPATH, elements.Ch_LoginPage_Register))).click()
                except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                    logger.error("未找到注册按钮")
                    pytest.fail("没有找到注册按钮")
            elif app_language == 'English':
                try:
                    WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located((By.XPATH, elements.En_LoginPage_Register))).click()
                    driver.press_keycode(4)
                    WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located((By.XPATH, elements.En_LoginPage_Register))).click()
                except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                    logger.error("未找到注册按钮")
                    pytest.fail("没有找到注册按钮")
            else:
                logger.error("请配置正确的语言")

        return _goto_register_page

    def register_method_switch(self):
        # TODO 需要根据register_type进行切换注册方式
        pass

    # 手机区号根据x、y点击
    @staticmethod
    def xy_click(driver, x=None, y=None):
        # 获取手机屏幕像素
        screen_size = driver.get_window_size()
        screen_width = screen_size["width"]
        screen_height = screen_size["height"]
        print(f"手机像素为：{screen_height} * {screen_width}")
        touch = TouchAction(driver)
        touch.tap(x=x, y=y).perform()

    def area_code_select(self, driver, elements, app_language, logger, region):
        try:
            if region == "Chinese":
                code_text = "China"
            elif region == "English":
                code_text = "USA"
            else:
                code_text = None
                logger.error("请输入国家名称或国家代号")
            # 出于未知原因导致元素无法正常定位到，使用x、y点击
            if app_language == "English":
                WebDriverWait(driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, elements.En_Phone_Register_AreaCodeList))
                ).click()
                sleep(0.5)
                self.xy_click(driver, 500, 1090)
                logger.info("已点击搜索框")
                # 选择区号
                self.virtural_keyboard_input(driver, code_text)
                logger.info("已发送搜索文本")
                driver.hide_keyboard()
                logger.info("已关闭虚拟键盘")
                sleep(0.5)
                self.xy_click(driver, 500, 1370)
            elif app_language == "Chinese":
                driver.find_element(By.XPATH, elements.Ch_Phone_Register_AreaCodeList).click()
                sleep(0.5)
                self.xy_click(driver, 500, 1080)
                logger.info("已点击搜索框")
                # 选择区号
                self.virtural_keyboard_input(driver, code_text)
                logger.info("已发送搜索文本")
                driver.hide_keyboard()
                logger.info("已关闭虚拟键盘")
                sleep(0.5)
                self.xy_click(driver, 500, 1370)
            else:
                logger.error("请输入正确的语言")
        except (selenium.common.exceptions.TimeoutException,
                selenium.common.exceptions.NoSuchElementException):
            logger.error("未找到区号列表")
            pytest.fail("未找到区号列表")


    # 使用虚拟键盘输入数字
    def virtural_keyboard_input(self, driver, data):
        keys = Config.Config.key
        is_complete = False
        for key, value in keys.items():
            if key == data:
                driver.press_keycode(value)
                is_complete = True
                break
        if not is_complete:
            data = list(data)
            for i in data:
                if i in keys:
                    key_code = keys[i]
                    driver.press_keycode(key_code)
                else:
                    raise ValueError("输入值没有对应的字典")


    # 输入手机号
    def phone_number_input(self, driver, elements, app_language, phone, logger):
        if app_language == "English":
            element = elements.En_Phone_Register_PhoneNumber
        elif app_language == "Chinese":
            element = elements.Ch_Phone_Register_PhoneNumber
        else:
            logger.error("请选择语言")
            element = None
        try:
            logger.info(f"xpath：{element}")
            driver.find_element(By.XPATH, element).click()
            logger.info("已点击手机号输入框")
            # 由于文本框不支持sendkeys操作，所以使用虚拟键盘输入
            self.virtural_keyboard_input(driver, phone)
            logger.info("已输入手机号")
            driver.hide_keyboard()
            logger.info("已关闭虚拟键盘")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException) as e:
            logger.error(f"未找到手机号输入框,异常：{e}")


    def nickname_input(self, driver, elements, nickname, logger):
        try:
            driver.find_element(By.XPATH, elements.Ch_Phone_Register_Nickname).send_keys(nickname)
            logger.info("已输入昵称")
        except(selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            logger.error("未找到昵称输入框")
            pytest.fail("未找到昵称输入框")

    def password_input(self, driver, elements, password, logger):
        try:
            WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, elements.Ch_Phone_Register_Passwd))
            ).send_keys(password)
            logger.info("已输入密码")
        except(selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找到密码输入框")
            pytest.fail("未找到密码输入框")

    def confirm_password_input(self, driver, elements, password, logger):
        try:
            elements = WebDriverWait(driver, 10).until(
                ec.visibility_of_all_elements_located((By.CLASS_NAME, elements.Ch_Phone_Register_ConfirmPasswd))
            )
            elements[3].send_keys(password)
            logger.info("已输入确认密码")
        except(selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找到确认密码输入框")
            pytest.fail("未找到确认密码输入框")

    def region_selection(self, driver, elements, logger, region):
        if region == "Chinese":
            region_element = elements.Phone_Region_Selection_China
        elif region == "English":
            region_element = elements.Phone_Region_Selection_America
        else:
            region_element = elements.Phone_Region_Selection_Cancel
            logger.error("没有地域信息，取消地域操作")
        try:
            s = WebDriverWait(driver, 10).until(
                ec.visibility_of_all_elements_located((By.CSS_SELECTOR, elements.Ch_Phone_Register_Region))
            )
            s[0].click()
            logger.info("已点击地区")
            WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, region_element))
            ).click()
            logger.info("已选择地区")
        except(selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找地区相关元素")
            pytest.fail("未找地区相关元素")

    def test_casse(self, setup, info):
        app_language, region, elements, tips_element, config = info
        driver = setup["driver"]
        logger = setup["logger"]
        self.area_code_select(driver, elements, app_language, logger, "Chinese")
        self.phone_number_input(driver, elements, app_language, config.phone, logger)
        self.nickname_input(driver, elements, config.nick_name, logger)
        self.password_input(driver, elements, config.phone_password, logger)
        self.confirm_password_input(driver, elements, config.phone_confirm_password, logger)
        self.region_selection(driver, elements, logger, region)
