from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AssignmentPage:
    def __init__(self, driver):
        self.driver = driver

    choose_course_ipt = (By.CSS_SELECTOR, "div[class*='css-1v4ccyo']")

    def choose_course(self,course):
        path =  "//li[text()='" + course + "']"
        self.driver.find_element(*AssignmentPage.choose_course_ipt).click()
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((
            By.XPATH, path))).click()



