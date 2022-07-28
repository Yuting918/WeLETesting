import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("/Applications/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("http://testsupport1lx.wri.wolfram.com:3089/login")
    # driver.maximize_window()
    request.cls.driver = driver

    yield

    # driver.close()
