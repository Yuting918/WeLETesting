from selenium.webdriver.common.by import By


class AddRolePage:
    def __init__(self,driver):
        self.driver = driver

    def select_option(self):
        self.driver.find_element(By.CSS_SELECTOR,"div["
                                                 "class*='css-182didf']").click()
