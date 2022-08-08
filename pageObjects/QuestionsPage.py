import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QuestionsPage:
    def __init__(self,driver):
        self.driver = driver

    choose_tags_ipt = (By.CSS_SELECTOR,"input[placeholder='Choose Tags:']")
    fetch_question_but = (By.XPATH, "//button[text()='Fetch Questions']")
    question_per_page = (By.ID,"demo-select-small")
    delete_buts = (By.XPATH,"//button[text()='Delete']")
    ok_but = (By.XPATH,"//button[text()='Ok']")

    def choose_tag(self,tag):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            QuestionsPage.choose_tags_ipt)).send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        self.driver.find_element(*QuestionsPage.choose_tags_ipt).send_keys(tag)
        self.driver.find_element(*QuestionsPage.choose_tags_ipt).send_keys(
            Keys.ARROW_DOWN,Keys.ENTER)

    def fetch_questions(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(
            QuestionsPage.fetch_question_but)).click()
        time.sleep(3)

    def delete_question(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            QuestionsPage.delete_buts)).click()
        time.sleep(1)
        self.driver.find_element(*QuestionsPage.ok_but).click()
        time.sleep(1)




