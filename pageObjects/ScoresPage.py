import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.TakingTestPage import TakingTestPage


class ScoresPage:
    def __init__(self, driver):
        self.driver = driver

    choose_course_ipt = (By.CSS_SELECTOR,"div[aria-haspopup='listbox']")
    fetch_score_but = (By.XPATH,"//button[text()='Fetch Score']")
    end_date_ipt = (By.XPATH,"(//input[@placeholder = 'mm/dd/yyyy'])[2]")
    score_rows = (By.XPATH,"//tbody//tr")

    def choose_course(self,course_name):
        self.driver.find_element(*ScoresPage.choose_course_ipt).click()
        path = "//li[text()='" + course_name +"']"
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((
            By.XPATH,path))).click()

    def set_end_date(self,end_date='01012023'):
        source = self.driver.find_element(*ScoresPage.end_date_ipt)
        source.click()
        source.send_keys(Keys.COMMAND + "a")
        source.send_keys(end_date)
        time.sleep(1)

    def fetch_score(self):
        self.driver.find_element(*ScoresPage.fetch_score_but).click()

    def get_score_rows(self):
        return self.driver.find_elements(*ScoresPage.score_rows)





