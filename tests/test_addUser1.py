import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from utilities.BaseClass import BaseClass

class TestAddUser(BaseClass):
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
            manageUserPage.submit_add_user()
        self.logout()





