from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TakingTestPage:
    def __init__(self, driver):
        self.driver = driver

    assignment_info_panel = (By.CLASS_NAME, ".test_examPropContainer__u2i_k")
    assignment_info = (By.CLASS_NAME, 'test_propdata__J9dM8')
    assignment_review = (By.CLASS_NAME, "submissionReview_reviewText__wX0vb")
    assignment_review_info = (By.CLASS_NAME,
                            "submissionReview_propDataText__lHUaZ")
    retake_assignment_but = (By.XPATH, "//button[text()='Retake Assignment']")
    question_ipt = (
    By.CSS_SELECTOR, "input[placeholder='Type your answer here']")
    submit_assignment_but = (By.XPATH,"//button[text()='Submit Assignment']")
    submit_assignment_conf_but = (By.XPATH, "//button[text()='Submit']")


    def get_assignment_info(self):
        infos = self.driver.find_elements(*TakingTestPage.assignment_info)
        info_list = []
        for info in infos:
            info_text = info.text
            info_list.append(info_text)
        return info_list

    def get_assignment_review(self):
        self.driver.find_element(*TakingTestPage.assignment_review)
        review_infos = self.driver.find_elements(
            *TakingTestPage.assignment_review_info)
        info_list=[]
        for info in review_infos:
            info_text = info.text
            info_list.append(info_text)
        return info_list


    def retake_assignment(self):
        self.driver.find_element(*TakingTestPage.retake_assignment_but).click()

    def type_answer(self, answer):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            TakingTestPage.question_ipt)).send_keys(answer)

    def submit_assignment(self):
        self.driver.find_element(*TakingTestPage.submit_assignment_but).click()

    def confirm_submit(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(
            TakingTestPage.submit_assignment_conf_but)).click()










