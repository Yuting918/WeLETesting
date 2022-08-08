import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.AddRolePage import AddRolePage
from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from testData.QuestionPoolData import QuestionPoolData
from utilities.BaseClass import BaseClass

class TestWeLEAdmin(BaseClass):
    course_name: str = 'TestCourse003'
    def test_admin_create_course(self, course_name=course_name):
        # log in as admin
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        manageCoursePage = dashboard.go_to_mangage_course()
        manageCoursePage.add_new_course()
        manageCoursePage.create_course(course_name,'Fall','TestTA',
                                       course_name+'_ID',
                                       "TestInstructor")
        self.logout()

    def test_admin_add_user(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        manageUserPage = dashboard.manage_user()
        manageUserPage.add_user('student')
        users = NewUserData.gen_user('Stu',39,41)

        for user in users:
            time.sleep(2)
            manageUserPage.get_ID().send_keys(user['ID'])
            manageUserPage.get_f_name().send_keys(user['f_name'])
            manageUserPage.get_l_name().send_keys(user['l_name'])
            log.info(user['ID'] + 'successfully added')
            time.sleep(2)
            manageUserPage.submit_add_user()
        self.logout()

    def test_admin_add_user_to_course(self, course_name=course_name):
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole("TestAdmin")
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        manageUserPage = dashboard.manage_user()
        users = NewUserData.gen_user('Stu',37,39)

        for user in users:
            manageUserPage.select_user(user['f_name'], user['l_name'])
            manageUserPage.select_course(course_name)
            time.sleep(1)
            popped_course = manageUserPage.get_popped_course()
            log.info('the popped course is: ' + popped_course)
            assert course_name in popped_course
            manageUserPage.submit_register_user()
            time.sleep(1)
            manageUserPage.sort_user()
            time.sleep(1)
            manageUserPage.sort_user()
            time.sleep(1)
            assert user['f_name'] in manageUserPage.get_registered_user(user[
                                                                         'f_name'])
            log.info(user['f_name'] + 'successfully added to' + course_name)
            self.driver.refresh()
            time.sleep(1)
        manageUserPage.logout()

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
        self.delete_all_pools(questionPoolPage,log)
        questionPoolPage.add_pool()
        question_pool_names = QuestionPoolData.pool_name_generator(2)
        log.info(question_pool_names)
        i = 0
        for p_name in question_pool_names:
            if i == 0:
                questionPoolPage.create_pool(p_name, 'TestPool',2)
            else:
                questionPoolPage.create_another_pool(p_name, 'TestPool',2)
            i += 1
        questionPoolPage.add_question()
        questionPoolPage.choose_tag('MATH 101')
        questionPoolPage.fetch_questions()
        self.add_all_questions(questionPoolPage,log)
        self.driver.find_element(By.TAG_NAME,'body').send_keys(
            Keys.CONTROL + Keys.HOME)
        self.driver.maximize_window()
        questionPoolPage.update_pool()
        self.logout()

    def test_generate_question_pool(self, course_name=course_name):
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
        assignmentConfigurePage.configure_assignment(course_name,
                                                     course_name+'_Ass_001',
                                               3,'Homework',True,2,
                                               '08202022',
                                               '08202022','Max')
        assignmentConfigurePage.save_and_proceed()
        assignmentConfigurePage.release_assignment()
        log.info('Assignment successfully released')





