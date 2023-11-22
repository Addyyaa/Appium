from Init import get_driver
from VersionSelection import VersionSelection
from LoginPage import LoginPage
Language = 'Chinese'
Vesions = 'Chinese'
Agreement = False
driver = get_driver()
version = VersionSelection(driver)
version.version_selection(version=Vesions, language=Language)
login = LoginPage(driver)
if Agreement == True:
    login.login("code", Language, Agreement)
elif Agreement == False:
    login.login("code", Language)
else:
    print("Agreement 变量错误！！！")




