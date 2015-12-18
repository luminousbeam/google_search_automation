from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

class GoogleSearch(object):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []

        self.accept_next_alert = True

    def test_google_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("python")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("python")
        driver.find_element_by_name("btnG").click()
        driver.find_element_by_link_text("Python tutorial - TutorialsPoint").click()
        driver.find_element_by_link_text("Python - Overview").click()
        driver.find_element_by_link_text("Python - Dictionary").click()

#if __name__ == "__main__":
