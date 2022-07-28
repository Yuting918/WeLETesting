import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
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
        manageUserPage.select_user(getData['f_name'], getData['l_name'])
        course_name = 'Mathematica 101'
        manageUserPage.select_course(course_name)
        time.sleep(1)
        popped_course = manageUserPage.get_popped_course()
        log.info('the popped course is: ' + popped_course)
        assert course_name in popped_course
        manageUserPage.submit_register_user()
        time.sleep(1)
        manageUserPage.sort_user()
        time.sleep(1)
        manageUserPage.sort_user()
        time.sleep(1)
        assert getData['f_name'] in manageUserPage.get_registered_user(getData['f_name'])
        log.info(getData['f_name'] + 'successfully added to' + course_name)
        self.logout()
        time.sleep(1)

    @pytest.fixture(params=NewUserData.new_student_user)
    def getData(self,request):
        return request.param