
import Init
import Element
import Config
import pytest
import logging
import VersionSelection
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

class TestChineseRegisterPage:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        driver = Init.get_driver()
        version = VersionSelection.VersionSelection(driver)
        version.version_selection("Chinese", "Chinese")
        element = Element.Element_version
        # 账号及密码
        email = Config.Config.email
        email_password = Config.Config.email_password
        email_confirm_password = Config.Config.email_confirm_password
        phone = Config.Config.phone
        phone_password = Config.Config.phone_password
        phone_confirm_password = Config.Config.phone_confirm_password
        nick_name = Config.Config.nick_name
        code_text = Config.Config.area_code_searchtext
        # TODO 需要对验证码重新设计，验证码输入、不输入、没点击获取验证码
        verify_code = Config.Config.verify_code
        # 进入注册界面
        driver.find_element(by='xpath', value=element.Ch_LoginPage_Register).click()
        logger = logging.getLogger(__name__)
        yield {
            "driver": driver,
            "element": element,
            "email": email,
            "email_password": email_password,
            "email_confirm_password": email_confirm_password,
            "phone": phone,
            "phone_password": phone_password,
            "phone_confirm_password": phone_confirm_password,
            "nick_name": nick_name,
            "verify_code": verify_code,
            "code_text": code_text,
            "logger": logger
        }
        driver.quit()

    # 手机区号根据x、y点击
    def area_code_click(self, setup):
        x = 500
        y = 1090
        touch = TouchAction(setup["driver"])
        touch.tap(x=x, y=y).perform()
    # 中文国内手机注册流程

    def chlanguage_chregion_phone_regist(self, setup, get_verify_code=False):

        setup["logger"] = logging.getLogger(__name__)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_AreaCodeList).click()
        setup["logger"].info("已展开区号列表")
        sleep(1)
        self.area_code_click(setup)
        setup["logger"].info("已点击搜索框")
        setup["driver"].implicitly_wait(10)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_AreaCode_Search).send_keys(
            setup["code_text"])
        setup["logger"].info("已发送搜索文本")
        setup["driver"].hide_keyboard()
        setup["logger"].info("已关闭虚拟键盘")
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_86).click()
        setup["logger"].info("已选择区号")
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_PhoneNumber).click()
        setup["driver"].implicitly_wait(1)
        setup["logger"].info("已点击手机号输入框")
        # 由于文本框不支持sendkeys，所以使用虚拟键盘输入
        for digit in setup["phone"]:
            digit = int(digit)
            key_code = digit + 7  # 转换成对应的键码
            setup["driver"].press_keycode(key_code)
        setup["logger"].info("已输入手机号")
        setup["driver"].hide_keyboard()
        setup["logger"].info("已关闭虚拟键盘")
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Nickname).send_keys(setup["nick_name"])
        setup["logger"].info("已输入昵称")
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Passwd).send_keys(setup["phone_password"])
        setup["logger"].info("已输入密码")
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_ConfirmPasswd).send_keys(
            setup["phone_confirm_password"])
        setup["logger"].info("已输入确认密码")
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_Region).click()
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_RegionChina).click()
        if get_verify_code == True:
            setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_GetCode).click()
            setup["logger"].info("已点击获取验证码")
        else:
            pass



    # 用例1：正确输入所有信息
    def test_chlanguage_chregion_phone_regist(self, setup):
        setup["phone"] = "12345678901"
        self.chlanguage_chregion_phone_regist(setup)





# class TestEnglishRegisterPage:
#     def __init__(self):
#         self.driver = Init.get_driver()
#         self.version = VersionSelection.VersionSelection(self.driver)
#         self.version.version_selection("Chinese", "English")