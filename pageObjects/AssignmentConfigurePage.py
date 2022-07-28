import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class AssignmentConfigurePage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    course_name = (By.ID, "autocomplete-course-field")
    assignment_name = (By.CSS_SELECTOR, "input[id='assignment-name']")
    max_attempt = (By.CSS_SELECTOR, "input[id='max-attempts-allowed']")
    ass_type = (By.CSS_SELECTOR, "label[class*='css-1jaw3da']")
    timer = (By.CSS_SELECTOR, "input[type='checkbox']")
    duration = (By.CSS_SELECTOR, "input[name='duration']")
    due_date = (By.XPATH, "(//input[@placeholder = "
                                          "'mm/dd/yyyy'])[1]")
    exd_due_date = (By.XPATH, "(//input[@placeholder = "
                                          "'mm/dd/yyyy'])[2]")
    grade_method = (By.CSS_SELECTOR, "div[role='button']")
    prequisite = (By.XPATH, "//button[text()='Add Prequisites']")
    save_pcd_but = (By.XPATH, "//button[text()='Save and Proceed']")
    save_ass_but = (By.XPATH, "//button[text()='Save']")
    release_ass_but = (By.XPATH, "//button[text()='Release']")

    def configure_assignment(self, course_name,ass_name,max_attempt,type,
                             timer,duration,due,etd_due,grade_method):
        self.add_course_name(course_name)
        time.sleep(1)
        self.add_assignment_name(ass_name)
        time.sleep(1)
        self.add_max_attempt(max_attempt)
        time.sleep(1)
        self.add_ass_type(type)
        time.sleep(1)
        if timer:
            self.enable_timer()
        time.sleep(1)
        self.add_duration(duration)
        time.sleep(1)
        self.add_due_date(due)
        time.sleep(1)
        self.add_extd_due_date(etd_due)
        time.sleep(1)
        self.add_grade_method(grade_method)
        time.sleep(1)

    def save_and_proceed(self):
        self.driver.find_element(*AssignmentConfigurePage.save_pcd_but).click()

    def save_assignment(self):
        self.driver.find_element(*AssignmentConfigurePage.save_ass_but).click()

    def release_assignment(self):
        self.driver.find_element(*AssignmentConfigurePage.release_ass_but).click()

    def add_assignment_name(self, ass_name):
        self.driver.find_element(
            *AssignmentConfigurePage.assignment_name).send_keys(ass_name)



    def add_course_name(self,course_name):
        self.driver.find_element(*AssignmentConfigurePage.course_name).send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteCoursePresence()
        self.driver.find_element(*AssignmentConfigurePage.course_name).send_keys(
            course_name)
        self.driver.find_element(*AssignmentConfigurePage.course_name).send_keys(
            Keys.ARROW_DOWN,Keys.ENTER)


    def add_ass_type(self, type):
        match type:
            case 'Quiz':
                i = 1
            case 'Homework':
                i = 2
            case 'Practice':
                i = 3
            case 'Exam':
                i = 4
        path = "label[class*='css-1jaw3da']:nth-child({0})".format(i)
        self.driver.find_element(By.CSS_SELECTOR, path).click()

    def add_max_attempt(self, max_attempt):
        self.driver.find_element(
            *AssignmentConfigurePage.max_attempt).send_keys(Keys.BACKSPACE)
        self.driver.find_element(
            *AssignmentConfigurePage.max_attempt).send_keys(max_attempt)

    def enable_timer(self):
        self.driver.find_element(*AssignmentConfigurePage.timer).click()

    def add_duration(self, duration):
        self.driver.find_element(
            *AssignmentConfigurePage.duration).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*AssignmentConfigurePage.duration).send_keys(
            duration)

    def add_due_date(self, due_date):
        source = self.driver.find_element(*AssignmentConfigurePage.due_date)
        source.click()
        source.send_keys(Keys.COMMAND + "a")
        source.send_keys(due_date)

    def add_extd_due_date(self, extd_due_date):
        source = self.driver.find_element(*AssignmentConfigurePage.exd_due_date)
        source.click()
        source.send_keys(Keys.COMMAND + "a")
        source.send_keys(extd_due_date)

    def add_grade_method(self, g_mtd):
        path = "li[data-value='{0}']".format(g_mtd)
        self.driver.find_element(*AssignmentConfigurePage.grade_method).click()
        self.driver.find_element(By.CSS_SELECTOR, path).click()