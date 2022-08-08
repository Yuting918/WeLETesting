import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.AddRolePage import AddRolePage
from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from utilities.BaseClass import BaseClass

class TestWeLEAdmin(BaseClass):
    # def test_admin_create_course(self):
    #     # log in as admin
    #     log = self.getLogger()
    #     loginPage = LoginPage(self.driver)
    #     self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
    #         Keys.ARROW_DOWN)
    #     self.verifyAutoCompleteUserPresence()
    #     loginPage.typeRole("TestAdmin")
    #     loginPage.chooseRole()
    #     dashboard = loginPage.logIn()
    #     manageCoursePage = dashboard.go_to_mangage_course()
    #     manageCoursePage.add_new_course()
    #     manageCoursePage.create_course('Test001','Fall','TestTA','TestN001',
    #                                    'TestInstructor')
    #     self.logout()

    def test_admin_add_user(self):
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
        users = NewUserData.new_student_user

        for user in users:
            manageUserPage.get_ID().send_keys(user['ID'])
            manageUserPage.get_f_name().send_keys(user['f_name'])
            manageUserPage.get_l_name().send_keys(user['l_name'])
            log.info(user['ID'] + 'successfully added')
            time.sleep(2)
            manageUserPage.submit_add_user()
        self.logout()

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
            course_name = 'Test001'
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
