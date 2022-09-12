import time

from selenium.webdriver.common.by import By

from pageObjects.AssignmentPage import AssignmentPage
from pageObjects.ManageCoursePage import ManageCoursePage
from pageObjects.ManageUserPage import ManageUserPage
from pageObjects.NewAssignmentPage import NewAssignmentPage
from pageObjects.QuestionPoolPage import QuestionPoolPage
from pageObjects.QuestionsPage import QuestionsPage
from pageObjects.RolePage import RolePage



class CoursesPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_course(self,name,ss=False,ssName=''):
        self.driver.find_element(By.XPATH,"//span[text()='"+name+"']").click()
        if ss:
            time.sleep(1.5)
            self.driver.save_screenshot(ssName)