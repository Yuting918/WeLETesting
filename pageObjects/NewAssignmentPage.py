import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.AssignmentConfigurePage import AssignmentConfigurePage
from utilities.BaseClass import BaseClass


class NewAssignmentPage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    choose_question_from = (By.CSS_SELECTOR, "div[class*='css-182didf']")
    question_bank = (By.XPATH, "//li[text()='Question Bank']")
    question_pool = (By.XPATH, "//li[text()='Question Pool']")
    question_pool_divs = (By.CSS_SELECTOR, "div[class*='assignmentSelectQuestions_questionRow__bVPre']")
    more_but = (By.XPATH,"//button[text()='More']")
    q_pool_label_from_div = (By.CSS_SELECTOR, "span[aria-label='TestPool000']")
    q_pool_add_from_div = (By.XPATH, "//button[text()='Add']")
    save_pcd_but = (By.XPATH, "//button[text()='Save and Proceed']")
    pool_name_ipt = (By.CSS_SELECTOR,"input[name='poolName']")
    fetech_pool_but = (By.XPATH, "//button[text()='Fetch Pools']")


    def choose_from_q_bank(self):
        self.driver.find_element(*NewAssignmentPage.choose_question_from).click()
        self.driver.find_element(*NewAssignmentPage.question_bank).lick()

    def choose_from_q_pool(self):
        self.driver.find_element(*NewAssignmentPage.choose_question_from).click()
        self.driver.find_element(*NewAssignmentPage.question_pool).click()

    def get_pool_by_name(self,pool_name):
        self.driver.find_element(*NewAssignmentPage.more_but).click()
        self.driver.find_element(*NewAssignmentPage.pool_name_ipt).send_keys(
            pool_name)
        self.driver.find_element(*NewAssignmentPage.fetech_pool_but).click()
        q_pools = self.driver.find_elements(
            *NewAssignmentPage.question_pool_divs)
        for q_pool in q_pools:
            label = q_pool.find_element(*NewAssignmentPage.q_pool_label_from_div)
            log = self.getLogger()
            log.info(label.text)
            if label.text.upper() == pool_name.upper():
                q_pool.find_element(
                    *NewAssignmentPage.q_pool_add_from_div).click()


    def save_and_proceed(self):
        self.driver.find_element(*NewAssignmentPage.save_pcd_but).click()
        return AssignmentConfigurePage(self.driver)
















