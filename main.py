from Init import get_driver
from VersionSelection import VersionSelection
from LoginPage import LoginPage
import Config
Language = 'Chinese'
versions = 'Chinese'
Agreement_verifycode = (True, False)
Login_type = "code"
driver = get_driver()
version = VersionSelection(driver)
version.version_selection(version=versions, language=Language)
# 初始化一些变量
Config.Config.phone = "15250996930"
login = LoginPage(driver)
if Agreement_verifycode[0]:
    login.login(Login_type, Language, Agreement_verifycode)
elif not Agreement_verifycode[0]:
    login.login(Login_type, Language)
else:
    print("Agreement 变量错误！！！")




