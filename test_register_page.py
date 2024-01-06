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

    @pytest.fixture(scope="function", autouse=True)
    def content_clear(self, info):
        if "清理通知栏":
            app_language, region_info, elements, tips_element, config = info
            # 清理通知栏
            driver.open_notifications()
            logger.info("开始清理通知栏内容")
            try:
                self.wait_find("id", elements.notification_clear, 2).click()
            except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                logger.error("没有可清理的内容，退出通知栏")
                driver.press_keycode(4)
            logger.info("已清理通知栏内容")
        yield
        if "清理输入框":
            # 未防止在清理的过程中发生元素定位异常，故在各方法内实现清理
            pass

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
        data = str(data)
        keys = Config.Config.key
        is_complete = False
        for key, value in keys.items():
            if key == data:
                driver.press_keycode(value)
                driver.hide_keyboard()
                logger.info("已关闭虚拟键盘")
                is_complete = True
                break
        if not is_complete:
            data = list(data)
            for i in data:
                if i in keys:
                    key_code = keys[i]
                    driver.press_keycode(key_code)
                    driver.hide_keyboard()
                else:
                    raise ValueError(f"输入值没有对应的字典：i={i}，data={data}")

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
            s = self.wait_find('xpath', element)
            s.clear()
            s.click()
            logger.info("已点击手机号输入框")
            # 由于文本框不支持sendkeys操作，所以使用虚拟键盘输入
            self.virtural_keyboard_input(phone)
            logger.info("已输入手机号")
            self.phone = phone
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException) as e:
            logger.error(f"未找到手机号输入框,异常：{e}")

    @staticmethod
    def nickname_input(info, nickname):
        app_language, region_info, elements, tips_element, config = info
        try:
            s = driver.find_element(By.XPATH, elements.Ch_Phone_Register_Nickname)
            s.clear()
            s.send_keys(nickname)
            logger.info("已输入昵称")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            logger.error("未找到昵称输入框")
            pytest.fail("未找到昵称输入框")

    def password_input(self, info, password):
        app_language, region_info, elements, tips_element, config = info
        try:
            s = self.wait_find("xpath", elements.Ch_Phone_Register_Passwd)
            s.clear()
            s.send_keys(password)
            logger.info("已输入密码")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找到密码输入框")
            pytest.fail("未找到密码输入框")

    def confirm_password_input(self, info, password):
        app_language, region_info, elements, tips_element, config = info
        try:
            s = WebDriverWait(driver, 10).until(
                ec.visibility_of_all_elements_located((By.CLASS_NAME, elements.Ch_Phone_Register_ConfirmPasswd))
            )
            logger.info(f"{s[3].text}\n{s}")
            s[3].clear()
            s[3].send_keys(password)
            logger.info("已输入确认密码")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找到确认密码输入框")
            pytest.fail("未找到确认密码输入框")
        except selenium.common.exceptions.WebDriverException:
            logger.error("驱动异常，尝试第二遍查找")
            try:
                for i in range(1):
                    elements = WebDriverWait(driver, 10).until(
                        ec.visibility_of_all_elements_located((By.CLASS_NAME, elements.Ch_Phone_Register_ConfirmPasswd))
                    )
                    elements[3].clear()
                    elements[3].send_keys(password)
                    logger.info("已输入确认密码")
            except selenium.common.exceptions.WebDriverException:
                logger.error("二次查找失败，驱动仍然异常,使用xy点击")
                self.xy_click(46.30, 53.82)
                driver.hide_keyboard()
                self.virtural_keyboard_input("sf123123")
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
            for i in range(5):
                try:
                    s = self.wait_find('xpath', elements.Ch_Phone_Register_Region)
                    logger.info(f"元素为：{s}")
                    s.click()
                    if s:
                        break
                except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                    logger.error("未找地区相关元素")
                    logger.info(driver.page_source)
                    pytest.fail("未找地区相关元素")
            logger.info("已点击地区")
            sleep(0.5)
            self.wait_find('xpath', region_element).click()
            logger.info("已选择地区")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找地区相关元素")
            pytest.fail("未找地区相关元素")

    def verification_code_get(self, info):
        app_language, region_info, elements, tips_element, config = info
        try:
            for i in range(3):
                s = self.wait_find('xpath', elements.Phone_Register_GetCode)
                s.click()
                sleep(2)
                txt = s.text
                if txt is not None and txt != "":
                    logger.info(f"已点击获取验证码按钮，元素text：{txt}，type：{type(txt)}")
                    break
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找到获取验证码按钮")

    def verification_code_read(self, info):
        app_language, region_info, elements, tips_element, config = info
        logger.info("开始获取短信验证码")
        driver.open_notifications()
        logger.info("已打开通知栏")
        try:
            code = self.wait_find('xpath', elements.sms_code, 30)
            txt = code.text
            if code:
                pattern = r"码为：(\d+)"
                verify_code = re.search(pattern, txt).group(1)
                logger.info(f"验证码获取成功：{txt}，验证码为：{verify_code}")
                if verify_code:
                    logger.info("清除通知栏内容")
                    self.wait_find('id', elements.notification_clear, 5).click()
                    logger.info("已清除通知栏内容并已关闭")
                    self.verify_code = verify_code
                else:
                    logger.error("验证码获取失败，未能正则匹配到验证码")
            else:
                logger.error("验证码获取失败，未找到对应元素")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print(driver.page_source)
            logger.error("未找到短信验证码")
            pytest.fail("未找到短信验证码")

    def verification_code_input(self, info, *verify_code):
        if verify_code:
            verify_code = str(verify_code[0])
            logger.info(f"有验证码参数：{verify_code}")
        else:
            verify_code = self.verify_code
            logger.info(f"没有验证码参数，使用读取的验证码：{verify_code}")
        self.xy_click(27.78, 69.88)
        self.virtural_keyboard_input(verify_code)

    def phone_number_format_validation(self, info, *phone):
        app_language, region_info, elements, tips_element, config = info
        if phone:
            phone = str(phone[0])
            logger.info(f"使用新传入的手机号：{phone}")
        else:
            phone = self.phone
            logger.info(f"使用默认手机号：{phone}")
        phone = str(phone)
        if region_info == "Chinese":
            areacode = "86"
        elif region_info == "English":
            areacode = "1"
        else:
            areacode = "86"
            logger.error("未知地区,使用默认区号86校验")
        try:
            parsed_number = phonenumbers.parse(f"+{areacode}{phone}")
            is_valid_number = phonenumbers.is_valid_number(parsed_number)
            if is_valid_number:
                logger.info(f"号码：{phone}校验通过")
            else:
                logger.error(f"号码：{phone}校验失败")
            return is_valid_number
        except phonenumbers.NumberParseException as e:
            logging.error(f"号码解析异常{e}")
            pytest.fail("号码解析异常")

    def register_button_click(self, info):
        app_language, region_info, elements, tips_element, config = info
        for i in range(2):
            try:
                logger.info("开始点击注册按钮")
                s = self.wait_find('xpath', elements.Phone_RegisterButton)
                txt = s.text
                s.click()
                if txt is not None and txt != "":
                    logger.info(f"已点击注册按钮，元素text：{txt}，type：{type(txt)}")
                    break
            except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                print(driver.page_source)
                logger.error("未找到注册按钮")

    def user_agreement_checkbox(self, info, status="AGREE"):
        """
        用户协议勾选
        :param info: 必填
        :param status: AGREE 勾选用户协议，DISAGREE 取消勾选
        """
        app_language, region_info, elements, tips_element, config = info
        try:
            s = self.wait_find('xpath', elements.Phone_Register_useragree)
            txt = s.text
            if status.upper() == 'AGREE':
                if txt == "kegouxuan":
                    s.click()
                    logger.info("已勾选用户协议")
                elif txt == "gouxuanzhong":
                    logger.info("已勾选用户协议,无须再次勾选")
                else:
                    logger.error(f"未能正常勾选用户协议,原因为元素text获取异常{txt}")
            elif status.upper() == 'DISAGREE':
                if txt == "gouxuanzhong":
                    s.click()
                    logger.info("已勾选用户协议")
                elif txt == "kegouxuan":
                    logger.info("当前未处于勾选状态无需操作")
                else:
                    logger.error(f"未能正常勾选用户协议,原因为元素text获取异常{txt}")
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            logger.error("未找到用户协议复选框元素，尝试二次查找")
            for i in range(1):
                try:
                    s = self.wait_find('xpath', elements.Phone_Register_useragree)
                    txt = s.text
                    if status.upper() == 'AGREE':
                        if txt == "kegouxuan":
                            s.click()
                            logger.info("已勾选用户协议")
                        elif txt == "gouxuanzhong":
                            logger.info("已勾选用户协议,无须再次勾选")
                        else:
                            logger.error(f"未能正常勾选用户协议,原因为元素text获取异常{txt}")
                    elif status.upper() == 'DISAGREE':
                        if txt == "gouxuanzhong":
                            s.click()
                            logger.info("已勾选用户协议")
                        elif txt == "kegouxuan":
                            logger.info("当前未处于勾选状态无需操作")
                        else:
                            logger.error(f"未能正常勾选用户协议,原因为元素text获取异常{txt}")
                except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                    logger.error("二次定位用户协议复选框元素失败")
                    pytest.fail("未能成功定位到用户协议复选框")
            print(driver.page_source)
            logger.error("未找到用户协议复选框")
            pytest.fail("未找到用户协议复选框")

    def test_casse(self, setup, info):
        self.area_code_select(info, "Chinese")
        self.phone_number_input(info, 15250996938)
        self.nickname_input(info, Config.Config.nick_name)
        self.password_input(info, Config.Config.phone_password)
        self.confirm_password_input(info, Config.Config.phone_confirm_password)
        self.region_selection(info, "Chinese")
        # self.verification_code_get(info)
        # self.verification_code_read(info)
        # self.verification_code_input(info)
        self.phone_number_format_validation(info)
        self.user_agreement_checkbox(info)
        self.register_button_click(info)

    def test_case2(self, setup, info):
        self.phone_number_input(info, 12345678)
        self.phone_number_format_validation(info)
