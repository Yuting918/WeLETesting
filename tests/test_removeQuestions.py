import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.AddRolePage import AddRolePage
from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from utilities.BaseClass import BaseClass


class TestCreateRole(BaseClass):

    def test_admin_add_role(self):
        # login and get tabs
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        questionsPage = dashboard.go_to_question()
        questionsPage.choose_tag("ART101")
        questionsPage.fetch_questions()
        for i in range(5):
            time.sleep(2)
            questionsPage.delete_question()
