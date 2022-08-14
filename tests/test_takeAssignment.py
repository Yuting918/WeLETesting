import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.AddRolePage import AddRolePage
from pageObjects.LoginPage import LoginPage
from testData.NewUserData import NewUserData
from testData.AsStudentTestData import AsStudentTestData
from utilities.BaseClass import BaseClass

class TestTakeAssignment(BaseClass):

    def test_stu_take_ass_timer(self,getData):
        stu_id = getData['ID']
        student = 'StuFName'+stu_id+' StuLName'+stu_id
        course_name = 'TestCourse003'
        assignment_name = course_name+'_Ass_002'
        answer = getData['Answer']
        # log in as student
        log = self.getLogger()
        loginPage = LoginPage(self.driver)
        self.driver.find_element(By.ID, "autocomplete-user-field").send_keys(
            Keys.ARROW_DOWN)
        self.verifyAutoCompleteUserPresence()
        loginPage.typeRole(student)
        loginPage.chooseRole()
        dashboard = loginPage.logIn()
        tabs = dashboard.get_tab_buttons()
        tabs_l = []
        for tab in tabs:
            tabs_l.append(tab.text)
        log.info(tabs_l)

        # taking the test
        assignmentPage = dashboard.go_to_assignment()
        assignmentPage.choose_course(course_name)
        takingAssPage = assignmentPage.go_to_spec_ass(assignment_name)

        ass_info = takingAssPage.get_assignment_info()
        log.info(f'The assignment name is {ass_info[0]}; The type is '
                 f'{ass_info[1]}; The number of questions is {ass_info[2]}; '
                 f'The time limit is {ass_info[3]}')
        time_in_min = int(ass_info[3].split(' Minutes')[0])
        time_in_sec = time_in_min * 60
        takingAssPage.type_answer(answer)
        time.sleep(time_in_sec + 5)
        ass_r_info = takingAssPage.get_assignment_review()
        log.info(ass_r_info)
        actual_time_string = ass_r_info[5]
        actual_time_h = int(actual_time_string.split('h')[0])
        actual_time_m = int((actual_time_string.split('h ')[1]).split('min')[0])
        actual_time_s = int(((actual_time_string.split('h ')[1]).split('min '
                            '')[1]).split('sec')[0])
        actual_time_in_sec = actual_time_h*60*60 + actual_time_m*60 + actual_time_s

        assert abs(actual_time_in_sec - time_in_sec) < 10

    @pytest.fixture(params=AsStudentTestData.gen_id_answer(1,3,['-3/(x^4)',
                                                             '8x^7 +Cos[x]']))
    def getData(self, request):
        return request.param













