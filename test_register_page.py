import Init
import Element
import Config
import pytest
import logging
import VersionSelection


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
        phone = Config.Config.phone
        phone_password = Config.Config.phone_password
        nick_name = Config.Config.nick_name
        # TODO 需要对验证码重新设计，验证码输入、不输入、没点击获取验证码
        verify_code = Config.Config.verify_code
        logger = logging.getLogger(__name__)
        # 进入注册界面
        driver.find_element(by='xpath', value=element.Ch_LoginPage_Register).click()
        yield {
            "driver": driver,
            "element": element,
            "email": email,
            "email_password": email_password,
            "phone": phone,
            "phone_password": phone_password,
            "nick_name": nick_name,
            "verify_code": verify_code,
            "logger": logger
        }
        driver.quit()

    # 中文国内手机注册流程

    def test_chlanguage_chregion_phone_regist(self, setup):
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_AreaCodeList).click()
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_AreaCode_Search).send_keys("中国大陆")
        setup["driver"].implicitly_wait(1)
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Area_Code_86).click()
        setup["driver"].find_element(by='xpath', value=setup["element"].Ch_Phone_Register_PhoneNumber).send_keys(setup["phone"])

    def test_ppt(self):
        print("1")




# class TestEnglishRegisterPage:
#     def __init__(self):
#         self.driver = Init.get_driver()
#         self.version = VersionSelection.VersionSelection(self.driver)
#         self.version.version_selection("Chinese", "English")