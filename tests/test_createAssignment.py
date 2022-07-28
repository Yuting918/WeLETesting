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
        newAssignmentPage = dashboard.create_assignment_admin()
        newAssignmentPage.choose_from_q_pool()
        newAssignmentPage.get_pool_by_name('TestPool000')
        assignmentConfigurePage = newAssignmentPage.save_and_proceed()
        assignmentConfigurePage.configure_assignment('Mathematica 101','Math101_Ass1',
                                               3,'Homework',True,15,
                                               '08012022',
                                               '08012022','Max')
        assignmentConfigurePage.save_and_proceed()
        assignmentConfigurePage.release_assignment()
        log.info('Assignment successfully released')


