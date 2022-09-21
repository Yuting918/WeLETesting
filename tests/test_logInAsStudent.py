from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass

class TestAddUser(BaseClass):
    def test_admin_add_user(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestStudent1")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        self.logout()

