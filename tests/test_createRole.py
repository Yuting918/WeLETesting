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
        tabs = dashboard.get_tab_buttons()
        tabs_l = []
        for tab in tabs:
            tabs_l.append(tab.text)
        log.info(tabs_l)
        # Instructor, Teaching Assistant, Administrator
        self.view_roles('Administrator',log,dashboard)

        self.driver.find_element(By.CSS_SELECTOR,"button["
                                                 "class*='css-1jmdrwe']").click()
        addRolePage = AddRolePage(self.driver)







    def view_roles(self, role,log,dashboard):
        # create role
        rolePage = dashboard.view_role()
        roles = rolePage.get_roles()
        roleName = role

        for role in roles:
            if role.find_element(By.XPATH,"td/div/span").text == roleName:
                log.info(roleName)
                role.find_element(By.XPATH, "td/button").click()

        time.sleep(1)
        roleTitle = self.driver.find_element(By.CLASS_NAME,
                                           "adminRoleSlug_headingText__Oz7TX").text
        assert roleTitle == roleName







