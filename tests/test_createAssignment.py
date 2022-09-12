import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from testData.QuestionPoolData import QuestionPoolData
from utilities.BaseClass import BaseClass

class TestGenQuesPool(BaseClass):
    # choose based on the dashboard of admin
    def test_generate_question_pool(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        coursePage = dashboard.go_to_courses()
        coursePage.go_to_course('TestCourse2',True,
                                '/Users/yutingq/Desktop/lms_was_testing/createAssignment/before_create_assignment.png')
        newAssignmentPage = dashboard.create_assignment_admin()
        newAssignmentPage.choose_from_q_pool()
        newAssignmentPage.get_pool_by_name('TestPool001')
        assignmentConfigurePage = newAssignmentPage.save_and_proceed()
        assignmentConfigurePage.configure_assignment('TestCourse2',
                                                     'TestAss1Course2',
                                               3,'Homework',True,1,
                                               '09182023',
                                               '09182023','Max')
        assignmentConfigurePage.save_and_proceed()
        assignmentConfigurePage.release_assignment()
        log.info('Assignment successfully released')
        coursePage = dashboard.go_to_courses()
        coursePage.go_to_course('TestCourse2', True,
                                '/Users/yutingq/Desktop/lms_was_testing/createAssignment/after_create_assignment.png')


