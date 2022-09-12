import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from testData.QuestionPoolData import QuestionPoolData
from utilities.BaseClass import BaseClass

class TestGenQuesPool(BaseClass):
    def test_generate_question_pool(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        questionPoolPage = dashboard.go_to_ques_pool()
        questionPoolPage.add_pool()
        questionPoolPage.create_pool('TestPool003', 'TestPool003',1)
        # questionPoolPage.add_question()
        # questionPoolPage.choose_tag('MATH 101')
        # questionPoolPage.fetch_questions()
        self.add_all_questions(questionPoolPage,log)
        self.driver.find_element(By.TAG_NAME,'body').send_keys(
            Keys.CONTROL + Keys.HOME)
        self.driver.maximize_window()
        questionPoolPage.update_pool()
        self.driver.save_screenshot(
            '/Users/yutingq/Desktop/lms_was_testing/createQuestionPool'
            '/questionPoolCreated.png')





    def add_all_questions(self,questionPoolPage,log):
        while True:
            try:
                questionPoolPage.get_alert()
                log.info('No question fetched')
                break
            except:
                questionPoolPage.click_add()