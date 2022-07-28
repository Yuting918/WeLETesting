import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from utilities.BaseClass import BaseClass

class TestAddUser(BaseClass):

    def test_admin_add_user_to_course(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        manageUserPage = dashboard.manage_user()
        users = NewUserData.new_student_user

        for user in users:
            manageUserPage.select_user(user['f_name'], user['l_name'])
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
            assert user['f_name'] in manageUserPage.get_registered_user(user[
                                                                         'f_name'])
            log.info(user['f_name'] + 'successfully added to' + course_name)
            self.driver.refresh()
            time.sleep(1)
        manageUserPage.logout()

