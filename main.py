from Init import get_driver
from VersionSelection import VersionSelection
from LoginPage import LoginPage
import Config
Language = 'Chinese'
versions = 'Chinese'
Agreement_verifycode = (True, True)
# 决定是否获取验证码，是否填写验证码
getCode_fillCode = (True, True)

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




