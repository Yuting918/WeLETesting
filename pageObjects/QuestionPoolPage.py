import logging
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class QuestionPoolPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    add_pool_but = (By.XPATH, "//button[contains(text(), 'Add Pool')]")
    pool_name_ipt = (By.CSS_SELECTOR, "input[name='poolName']")
    pool_tag_ipt = (By.XPATH, "(//input[@id='asynchronous-demo'])[2]")
    max_score_ipt = (By.XPATH, "//input[@name='maxScore']")
    create_pool_but = (By.XPATH,"//button[contains(text(), 'Create New')]")
    create_another_pool_but = (By.XPATH, "//button[contains(text(), 'Create Another')]")
    insert_from_qbank_but = (By.XPATH,"//button[contains(text(), 'Insert from')]")
    tag_chooser = (By.XPATH, "(//div/input[@id='asynchronous-demo'])[2]")
    topic_chooser = (By.XPATH, "(//div/input[@id='asynchronous-demo'])[3]")
    fetch_q_but = (By.XPATH, "//button[contains(text(),'Fetch Questions')]")
    alert_info = (By.CSS_SELECTOR, "div[role='alert']")
    questions = (By.CSS_SELECTOR, "div[class*='questionPoolCardWithButton_summaryContainer__l6yhm']")
    pools = (By.CSS_SELECTOR, "div[class*='recentPoolCard_container__8DztQ']")
    view_pool_but = (By.LINK_TEXT,'View Pool')
    delete_pool_but = (By.XPATH, "//button[text()='Delete Pool']")
    confirm_delete_but = (By.XPATH, "//button[text()='Ok']")
    add_question_to_pool_but = (By.XPATH, "//button[text()='Add']")
    update_pool_but = (By.XPATH, "//button[text()='Update Pool']")


    def add_pool(self):
        self.driver.find_element(*QuestionPoolPage.add_pool_but).click()

    def create_pool(self,pool_name,pool_tag,pool_score):
        self.driver.find_element(*QuestionPoolPage.pool_name_ipt).send_keys(pool_name)
        self.driver.find_element(*QuestionPoolPage.pool_tag_ipt).click()
        self.driver.find_element(*QuestionPoolPage.pool_tag_ipt).send_keys(
            pool_tag,Keys.ENTER)
        self.driver.find_element(*QuestionPoolPage.max_score_ipt).click()
        self.driver.find_element(*QuestionPoolPage.max_score_ipt).send_keys(
            pool_score)
        self.driver.find_element(*QuestionPoolPage.create_pool_but).click()
        time.sleep(1)

    def create_another_pool(self,pool_name,pool_tag,pool_score):
        self.driver.find_element(
            *QuestionPoolPage.create_another_pool_but).click()
        self.driver.find_element(*QuestionPoolPage.pool_tag_ipt).click()
        self.driver.find_element(*QuestionPoolPage.pool_tag_ipt).send_keys(
            pool_tag, Keys.ENTER)
        self.driver.find_element(*QuestionPoolPage.max_score_ipt).click()
        self.driver.find_element(*QuestionPoolPage.max_score_ipt).send_keys(
            pool_score)
        self.driver.find_element(*QuestionPoolPage.create_pool_but).click()
        time.sleep(1)

    def add_question(self):
        self.driver.find_element(*QuestionPoolPage.insert_from_qbank_but).click()

    def choose_tag(self,tag):
        self.driver.find_element(*QuestionPoolPage.tag_chooser).send_keys(Keys.ARROW_DOWN)
        self.verifyADLPresence()
        self.driver.find_element(*QuestionPoolPage.tag_chooser).send_keys(tag)
        self.driver.find_element(*QuestionPoolPage.tag_chooser).send_keys(
            Keys.ARROW_DOWN,Keys.ENTER)

    def choose_topic(self,topic):
        self.driver.find_element(*QuestionPoolPage.topic_chooser).send_keys(
            Keys.ARROW_DOWN)
        self.verifyADLPresence()
        self.driver.find_element(*QuestionPoolPage.topic_chooser).send_keys(topic)
        self.driver.find_element(*QuestionPoolPage.topic_chooser).send_keys(
            Keys.ARROW_DOWN, Keys.ENTER)

    def fetch_questions(self):
        self.driver.find_element(*QuestionPoolPage.fetch_q_but).click()

    def get_alert(self):
        return self.driver.find_element(*QuestionPoolPage.alert_info)

    def get_questions(self):
        return self.driver.find_elements(*QuestionPoolPage.questions)

    def get_pools(self):
        return self.driver.find_element(*QuestionPoolPage.pools)

    def view_pool(self):
        self.driver.find_element(*QuestionPoolPage.view_pool_but).click()

    def delete_pool(self):
        self.driver.find_element(*QuestionPoolPage.delete_pool_but).click()
        self.driver.find_element(*QuestionPoolPage.confirm_delete_but).click()

    def click_add(self):
        self.driver.find_element(
            *QuestionPoolPage.add_question_to_pool_but).click()

    def update_pool(self):
        element =  self.driver.find_element(
            *QuestionPoolPage.update_pool_but)
        self.driver.execute_script("arguments[0].click();", element)













