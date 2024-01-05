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

logger = logging.getLogger(__name__)
driver = None


# noinspection PyTypeChecker,PyUnresolvedReferences
class TestRegister:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, goto_register_page, info):
        # 通过参数引用 goto_register_page fixture
        app_language, region, elements, tips_element, config = info
        global driver
        driver = Init.get_driver()
        driver.implicitly_wait(10)
        version = VersionSelection.VersionSelection(driver)
        version.version_selection(region, app_language)
        # 在 setup 中调用 goto_register_page
        goto_register_page(driver, elements, app_language)
        yield driver
        sleep(3)
        driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def info(self):
        app_language = "English"
        region = "Chinese"
        register_type = 'phone'
        elements = Element.Element_version
        tips_element = ElementTips.register_page_tips
        config = Config.Config
        return app_language, region, elements, tips_element, config

    # 定义为 fixture，并作为参数传递给 setup
    @pytest.fixture(scope="class", autouse=True)
    def goto_register_page(self):
        def _goto_register_page(driver, elements, app_language):
            try:
                if app_language == "Chinese":
                    self.wait_find("xpath", elements.Ch_LoginPage_Register).click()
                    driver.press_keycode(4)
                    self.wait_find("xpath", elements.Ch_LoginPage_Register).click()
                elif app_language == 'English':
                    self.wait_find("xpath", elements.En_LoginPage_Register).click()
                    driver.press_keycode(4)
                    self.wait_find("xpath", elements.En_LoginPage_Register).click()
                else:
                    logger.error("请配置正确的语言")
            except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                logger.error("未找到注册按钮")
                pytest.fail("没有找到注册按钮")

        return _goto_register_page

    @staticmethod
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

    def register_method_switch(self):
        # TODO 需要根据register_type进行切换注册方式
        pass

    # 手机区号根据x、y点击
    @staticmethod
    def xy_click(x=None, y=None):
        """
        当前手机像素为 1080 * 2304
        :param x: 横坐标百分比
        :param y: 纵坐标百分比
        """
        # 获取手机屏幕像素
        screen_size = driver.get_window_size()
        screen_width = screen_size["width"]
        screen_height = screen_size["height"]
        print(f"手机像素为：{screen_height} * {screen_width}")
        x = round(x * screen_width / 100)
        y = round(y * screen_height / 100)
        logger.info(f"x={x}, y={y}")
        touch = TouchAction(driver)
        touch.tap(x=x, y=y).perform()

    def area_code_select(self, info, region):
        app_language, region_info, elements, tips_element, config = info
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
                self.wait_find("xpath", elements.En_Phone_Register_AreaCodeList).click()
                sleep(0.5)
                self.xy_click(46.29, 47.31)
                logger.info("已点击搜索框")
                # 选择区号
                self.virtural_keyboard_input(code_text)
                logger.info("已发送搜索文本")
                driver.hide_keyboard()
                logger.info("已关闭虚拟键盘")
                sleep(0.5)
                self.xy_click(46.30, 59.46)
            elif app_language == "Chinese":
                driver.find_element(By.XPATH, elements.Ch_Phone_Register_AreaCodeList).click()
                sleep(0.5)
                self.xy_click(46.30, 46.88)
                logger.info("已点击搜索框")
                # 选择区号
                self.virtural_keyboard_input(code_text)
                logger.info("已发送搜索文本")
                driver.hide_keyboard()
                logger.info("已关闭虚拟键盘")
                sleep(0.5)
                self.xy_click(46.30, 59.46)
            else:
                logger.error("请输入正确的语言")
        except (selenium.common.exceptions.TimeoutException,
                selenium.common.exceptions.NoSuchElementException):
            logger.error("未找到区号列表")
            pytest.fail("未找到区号列表")

    # 使用虚拟键盘输入数字
    @staticmethod
    def virtural_keyboard_input(data):
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
    def phone_number_input(self, info, phone):
        app_language, region_info, elements, tips_element, config = info
        if app_language == "English":
            element = elements.En_Phone_Register_PhoneNumber
        elif app_language == "Chinese":
            element = elements.Ch_Phone_Register_PhoneNumber
        else:
            logger.error("请选择语言")
            element = None
        try:
            logger.info(f"xpath：{element}")
            self.wait_find('xpath', element).click()
            logger.info("已点击手机号输入框")
            # 由于文本框不支持sendkeys操作，所以使用虚拟键盘输入
            self.virtural_keyboard_input(phone)
            logger.info("已输入手机号")
            driver.hide_keyboard()
            logger.info("已关闭虚拟键盘")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException) as e:
            logger.error(f"未找到手机号输入框,异常：{e}")

    @staticmethod
    def nickname_input(info, nickname):
        app_language, region_info, elements, tips_element, config = info
        try:
            driver.find_element(By.XPATH, elements.Ch_Phone_Register_Nickname).send_keys(nickname)
            logger.info("已输入昵称")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            logger.error("未找到昵称输入框")
            pytest.fail("未找到昵称输入框")

    def password_input(self, info, password):
        app_language, region_info, elements, tips_element, config = info
        try:
            self.wait_find("xpath", elements.Ch_Phone_Register_Passwd).send_keys(password)
            logger.info("已输入密码")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找到密码输入框")
            pytest.fail("未找到密码输入框")

    @staticmethod
    def confirm_password_input(info, password):
        app_language, region_info, elements, tips_element, config = info
        try:
            elements = WebDriverWait(driver, 10).until(
                ec.visibility_of_all_elements_located((By.CLASS_NAME, elements.Ch_Phone_Register_ConfirmPasswd))
            )
            elements[3].send_keys(password)
            logger.info("已输入确认密码")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找到确认密码输入框")
            pytest.fail("未找到确认密码输入框")

    def region_selection(self, info, region):
        app_language, region_info, elements, tips_element, config = info
        if app_language == "Chinese" and region == "Chinese":
            region_element = elements.Phone_Region_Selection_China
        elif app_language == "Chinese" and region == "English":
            region_element = elements.Phone_Region_Selection_America
        elif app_language == "English" and region == "Chinese":
            region_element = elements.En_Phone_Region_Selection_China
        elif app_language == "English" and region == "English":
            region_element = elements.En_Phone_Region_Selection_America
        else:
            region_element = elements.Selection_Cancel
            logger.error("语言和版本不正确，取消地域操作")
        try:
            for i in range(3):
                try:
                    s = self.wait_find('xpath', elements.Ch_Phone_Register_Region)
                    logger.info(f"元素为：{s}")
                    s.click()
                    break
                except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                    print(driver.page_source)
                    logger.error("未找地区相关元素")
                    pytest.fail("未找地区相关元素")
            logger.info("已点击地区")
            sleep(0.5)
            self.wait_find('xpath', region_element).click()
            logger.info("已选择地区")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找地区相关元素")
            pytest.fail("未找地区相关元素")

    def verification_code_get(self):
        # TODO
        pass

    def verification_code_input(self):
        # TODO
        pass

    def register_button_click(self):
        # TODO
        pass

    def user_agreement_checkbox(self):
        # TODO
        pass

    def test_casse(self, setup, info):
        self.area_code_select(info, "Chinese")
        self.phone_number_input(info, Config.Config.phone)
        self.nickname_input(info, Config.Config.nick_name)
        self.password_input(info, Config.Config.phone_password)
        self.confirm_password_input(info, Config.Config.phone_confirm_password)
        self.region_selection(info, "English")
