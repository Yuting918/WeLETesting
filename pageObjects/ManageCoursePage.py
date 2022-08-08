import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


class ManageCoursePage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    add_new_but = (By.XPATH, "//button[text()='+ Add New']")
    course_name_field = (By.ID,"course-name-field")
    term_field = (By.CSS_SELECTOR, "div[role='button']")
    ta_field = (By.ID,"autocomplete-user-field")
    class_number_field = (By.ID,"class-number-field")
    save_changes_but = (By.XPATH,"//button[text()='Save Changes']")
    instructor_field = (By.XPATH,"(//input[@id='autocomplete-user-field'])[2]")

    def add_new_course(self):
        self.driver.find_element(*ManageCoursePage.add_new_but).click()

    def create_course(self,course_name,term,TA,course_number,instructor):
        self.driver.find_element(
            *ManageCoursePage.course_name_field).send_keys(course_name)
        self.driver.find_element(*ManageCoursePage.term_field).click()
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(
            (By.XPATH,f"//li[text()='{term}']")))
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,f"//li[text()='{term}']").click()

        self.driver.find_element(*ManageCoursePage.ta_field).click()
        self.verifyAutoCompleteUserPresence()
        self.driver.find_element(*ManageCoursePage.ta_field).send_keys(TA)
        self.driver.find_element(*ManageCoursePage.ta_field).send_keys(
            Keys.ARROW_DOWN,Keys.ENTER)

        time.sleep(1)
        self.driver.find_element(
            *ManageCoursePage.class_number_field).send_keys(course_number)

        time.sleep(1)
        self.driver.find_element(*ManageCoursePage.instructor_field).send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        self.driver.find_element(*ManageCoursePage.instructor_field).send_keys(
            instructor)
        self.driver.find_element(*ManageCoursePage.instructor_field).send_keys(
            Keys.ARROW_DOWN, Keys.ENTER)

        time.sleep(1)
        self.driver.find_element(*ManageCoursePage.save_changes_but).click()







