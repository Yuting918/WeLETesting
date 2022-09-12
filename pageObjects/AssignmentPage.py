import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ScoresPage import ScoresPage
from pageObjects.TakingTestPage import TakingTestPage


class AssignmentPage:
    def __init__(self, driver):
        self.driver = driver
    choose_course_ipt = (By.CSS_SELECTOR, "div[class*='css-182didf']")
    confirmation_but = (By.CSS_SELECTOR, "input[type='checkbox']")
    start_test_button = (By.XPATH, "//button[text()='Start Test']")
    scores_but = (By.LINK_TEXT,'SCORES')



    def choose_course(self,course):
        path =  "//li[text()='" + course + "']"
        self.driver.find_element(*AssignmentPage.choose_course_ipt).click()
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((
            By.XPATH, path))).click()

    def zero_remaining_attempts(self):
        path = "//span[text()='0']"
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
            By.XPATH, path)))

    def go_to_spec_ass(self,ass_name):
        path = "//span[text()='" + ass_name + "']"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, path))).click()
        self.driver.find_element(*AssignmentPage.confirmation_but).click()
        self.driver.find_element(*AssignmentPage.start_test_button).click()
        time.sleep(5)
        return TakingTestPage(self.driver)

    def go_to_score_page(self):
        self.driver.find_element(*AssignmentPage.scores_but).click()
        time.sleep(2)
        return ScoresPage(self.driver)













