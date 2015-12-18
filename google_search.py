from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

class GoogleSearch(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        logging.basicConfig(filename="search.log", level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')
        logging.info("START")

    def search_item(self, item):
        self.driver.get("https://www.google.com/")
        logging.info("This is google.com")
        print(self.driver.title)
        search_bar = self.driver.find_element_by_name("q")
        search_bar.send_keys(item)
        logging.info("typed %s into the search bar", item)
        search_bar.submit()

    def python_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("python"))
            print(self.driver.title)
        except:
            logging.error("No page found.")
        logging.info("Should be clicking the 'Welcome to Python.org' search result link.")
        self.driver.find_element_by_link_text("Welcome to Python.org").click()
        try:
            logging.info("We should be in the python.org page now")
            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "main-header"))
                    )
        except TimeoutException:
            logging.error("Did not find header class name in python.org site")
        print(self.driver.title)

    def ruby_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("ruby"))
            print(self.driver.title)
        except TimeoutException:
            logging.error("No page found.")
        logging.info("Should be clicking the 'Ruby Programming Language' search result link.")
        self.driver.find_element_by_link_text("Ruby Programming Language").click()
        try:
            logging.info("We should be in the rub-lang.org page now")
            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "header_content"))
                    )
        except TimeoutException:
            logging.error("Did not find header id name in ruby-lang.org site")
        print(self.driver.title)

    def javascript_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("javascript"))
            print(self.driver.title)
        except TimeoutException:
            logging.error("No page found.")
        logging.info("Should be clicking the 'JavaScript.com' search result link.")
        self.driver.find_element_by_link_text("JavaScript.com").click()
        try:
            logging.info("We should be in the javascript.com page now")
            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "split-cell"))
                    )
        except TimeoutException:
            logging.error("Did not find header class name in javascript.com site")
        print(self.driver.title)

    def java_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("java"))
            print(self.driver.title)
        except:
            logging.error("No page found.")
        logging.info("Should be clicking the 'Download Free Java Software' search result link.")
        self.driver.find_element_by_link_text("Download Free Java Software").click()
        try:
            logging.info("We should be in the java.com page now")
            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "jvh0"))
                    )
        except TimeoutException:
            logging.error("Did not find header class name in java.com site")
        print(self.driver.title)

    def elixir_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("elixir"))
            print(self.driver.title)
        except:
            logging.error("No page found.")
        logging.info("Should be clicking the 'Elixir' search result link.")
        self.driver.find_element_by_link_text("Elixir").click()
        try:
            logging.info("We should be in the elixir-lang.org page now")
            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "branding"))
                    )
        except:
            logging.error("Did not find header class name in elixir-lang.org site")
        print(self.driver.title)

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    search = GoogleSearch()
    try:
        search.search_item('python')
        search.python_page()
        search.search_item('ruby')
        search.ruby_page()
        search.search_item('javascript')
        search.javascript_page()
        search.search_item('java')
        search.java_page()
        search.search_item('elixir')
        search.elixir_page()
    finally:
        search.close()
