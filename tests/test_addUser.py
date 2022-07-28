import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from utilities.BaseClass import BaseClass

class TestAddUser(BaseClass):
    def test_admin_add_user(self,getData):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        manageUserPage = dashboard.manage_user()
        manageUserPage.add_user('student')

        manageUserPage.get_ID().send_keys(getData['ID'])
        manageUserPage.get_f_name().send_keys(getData['f_name'])
        manageUserPage.get_l_name().send_keys(getData['l_name'])
        log.info(getData['ID'] + 'successfully added')
        #
        # manageUserPage.get_ID().send_keys('Id01')
        # manageUserPage.get_f_name().send_keys('FName')
        # manageUserPage.get_l_name().send_keys('LName')

        manageUserPage.submit_add_user()
        self.logout()


    @pytest.fixture(params=NewUserData.new_student_user)
    def getData(self,request):
        return request.param




