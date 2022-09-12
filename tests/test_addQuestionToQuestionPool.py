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
        questionPoolPage = dashboard.go_to_ques_pool(screenshot=True,
                                                     fileName='/Users/yutingq/Desktop/lms_was_testing/addQuestionToPool/before_add_question.png')
        questionPoolPage.view_pool()
        questionPoolPage.edit_pool()
        questionPoolPage.choose_tag('MATH 101')
        questionPoolPage.fetch_questions()
        self.add_all_questions(questionPoolPage, log)
        self.driver.find_element(By.TAG_NAME,'body').send_keys(
            Keys.CONTROL + Keys.HOME)
        self.driver.maximize_window()
        questionPoolPage.update_pool()

    def add_all_questions(self,questionPoolPage,log):
        while True:
            alertText = questionPoolPage.get_final_alert()
            if alertText == 'No Questions Found matching the search Inputs. ' \
                             'Please search with different combinations !':
                log.info(alertText)
                log.info('NO MORE OTHER QUESTIONS')
                break
            else:
                questionPoolPage.click_add()
                log.info('One question being added')
