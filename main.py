from Init import get_driver
from VersionSelection import VersionSelection
from LoginPage import LoginPage
import Config
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s - %(exc_info)s')
# 版本选择
Language = 'Chinese'
versions = 'Chinese'
# 用户协议
Agreement_verifycode = (True, True)
# 决定是否获取验证码，是否填写验证码,第二个参数为non-custom为使用短信验证码，非non-custom为真是短信验证码，None为不填写验证码
getCode_fillCode = (True, None)
# 选择登录方式，email为邮箱登录，phone为手机号登录，code为验证码登录
Login_type = "code"
driver = get_driver()
version = VersionSelection(driver)
version.version_selection(version=versions, language=Language)
# 初始化一些变量
Config.Config.phone = "15250996938"
login = LoginPage(driver)
if Agreement_verifycode[0]:
    login.login(getCode_fillCode, Login_type, Language, Agreement_verifycode,)
elif not Agreement_verifycode[0]:
    login.login(Login_type, Language)
else:
    print("Agreement 变量错误！！！")
