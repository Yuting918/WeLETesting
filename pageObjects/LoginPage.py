import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.DashboardPage import DashboardPage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    inputBox = (By.CSS_SELECTOR, 'input[aria-activedescendant="autocomplete-user-field-option-0"]')
    poppedRole = (By.CSS_SELECTOR, "input[aria-controls='autocomplete-user-field-listbox']")
    loginBut = (By.CLASS_NAME,"css-79xub")


    def typeRole(self,role):
        self.driver.find_element(*LoginPage.inputBox).send_keys(role)

    def chooseRole(self):
        self.driver.find_element(*LoginPage.poppedRole).send_keys(
            Keys.ARROW_DOWN,Keys.ENTER)

    def logIn(self):
        self.driver.find_element(*LoginPage.loginBut).click()
        dashboardPage = DashboardPage(self.driver)
        return dashboardPage


