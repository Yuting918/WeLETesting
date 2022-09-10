import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.RolePage import RolePage
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass


class ManageUserPage(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    id = (By.XPATH, "(//input)[2]")
    f_name = (By.XPATH, "(//input)[3]")
    l_name = (By.XPATH, "(//input)[4]")
    add_user_but = (By.XPATH,"//button[text()='Add Users']")
    student = (By.XPATH,"//div/ul/li[text()='Student']")
    instructor = (By.XPATH, "//div/ul/li[text()='Instructor']")
    ta = (By.XPATH, "//div/ul/li[text()='Teaching Assistant']")
    admin = (By.XPATH, "//div/ul/li[text()='Administrator']")

   # Add Users

    def add_user(self,role):
        self.select_role()
        match role:
            case 'student':
                self.select_student()
            case 'ta':
                self.select_ta()
            case 'admin':
                self.select_admin()
            case 'instructor':
                self.select_instructor()

    def submit_add_user(self):
        time.sleep(1)
        self.driver.find_element(*ManageUserPage.add_user_but).click()

    def get_ID(self):
        return self.driver.find_element(*ManageUserPage.id)

    def get_f_name(self):
        return self.driver.find_element(*ManageUserPage.f_name)

    def get_l_name(self):
        return self.driver.find_element(*ManageUserPage.l_name)

    def select_role(self):
        self.driver.find_element(By.XPATH,"(//div[@role='button'])["
                                                "1]").click()

    def select_student(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
           ManageUserPage.student)).click()


    def select_instructor(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            ManageUserPage.instructor)).click()

    def select_ta(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            ManageUserPage.ta)).click()

    def select_admin(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            ManageUserPage.admin)).click()

    # Manage Users for Course
    popped_course = (By.CSS_SELECTOR, "div[class*='css-li77g6']")
    register_user_but = (By.XPATH,"//button[text()='Register User']")
    serial_no = (By.XPATH,"//div[text()='Serial No']")

    def select_user(self,f_name,l_name):
        name = f_name + ' ' + l_name
        self.driver.find_element(By.XPATH, "(//div/input)[5]").click()
        self.verifyAutoCompleteUserPresence()
        self.driver.find_element(By.XPATH,"(//div/input)[5]").send_keys(name,
                                                                        Keys.ARROW_DOWN,Keys.ENTER)
    def select_user(self,name):
        self.driver.find_element(By.XPATH, "(//div/input)[5]").click()
        self.verifyAutoCompleteUserPresence()
        self.driver.find_element(By.XPATH,"(//div/input)[5]").send_keys(name,
                                                                        Keys.ARROW_DOWN,Keys.ENTER)


    def select_course(self,course_name):
        self.driver.find_element(By.XPATH,"(//div[@role='button'])[2]").click()
        self.verifyDropdownPresence(course_name)

    def get_popped_course(self):
        return self.driver.find_element(*ManageUserPage.popped_course).text

    def submit_register_user(self):
        self.driver.find_element(*ManageUserPage.register_user_but).click()

    def sort_user(self):
        self.driver.find_element(*ManageUserPage.serial_no).click()

    def get_registered_user(self,name):
        path = "//*[contains(text(),'" + name + "')]"
        return self.driver.find_element(By.XPATH, path).text











