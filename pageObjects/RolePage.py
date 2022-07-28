from selenium.webdriver.common.by import By


class RolePage:
    def __init__(self, driver):
        self.driver = driver

    def get_roles(self):
        return self.driver.find_elements(By.XPATH, "//tbody/tr")


    def return_dashboard(self):
        return self.driver.find_element(By.XPATH,"//a[text()='Dashboard']").click()

