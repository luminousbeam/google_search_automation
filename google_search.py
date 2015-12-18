from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

# class GoogleSearch(object):
#     def __init__(self):
#         self.driver = webdriver.Firefox()
#         logging.basicConfig(filename="search.log", level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')
#         logging.info("START")

def search_item(self, item):
    self.driver.get("https://www.google.com/")
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys(item)
    search_bar.submit()

def find_python():
    driver.get("http://www.google.com/")
    logging.info("This is google.com")
    print(driver.title)
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("python")
    logging.info("typed python into the search bar")
    inputElement.submit()
    try:
        logging.info("Should be clicking the 'Welcome to Python.org' search result link.")
        WebDriverWait(driver, 10).until(EC.title_contains("python"))
        print(driver.title)
    except:
        logging.error("No page found.")
    driver.find_element_by_link_text("Welcome to Python.org").click()
    try:
        logging.info("We should be in the python.org page now")
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "main-header"))
                )
    except:
        logging.error("Did not find header class name in python.org site")
    print(driver.title)

def find_ruby():
    driver.get("http://www.google.com")
    logging.info("This is google.com")
    print(driver.title)
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("ruby")
    logging.info("typed ruby into the search bar")
    inputElement.submit()
    try:
        logging.info("Should be clicking the 'Ruby Programming Language' search result link.")
        WebDriverWait(driver, 10).until(EC.title_contains("ruby"))
        print(driver.title)
    except TimeoutException:
        logging.error("No page found.")
    driver.find_element_by_link_text("Ruby Programming Language").click()
    try:
        logging.info("We should be in the rub-lang.org page now")
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "header_content"))
                )
    except TimeoutException:
        logging.error("Did not find header id name in ruby-lang.org site")
    print(driver.title)

def find_javascript():
    driver.get("http://www.google.com")
    logging.info("This is google.com")
    print(driver.title)
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("javascript")
    logging.info("typed javascript into the search bar")
    inputElement.submit()
    try:
        logging.info("Should be clicking the 'JavaScript.com' search result link.")
        WebDriverWait(driver, 10).until(EC.title_contains("javascript"))
        print(driver.title)
    except TimeoutException:
        logging.error("No page found.")
    driver.find_element_by_link_text("JavaScript.com").click()
    try:
        logging.info("We should be in the javascript.com page now")
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "split-cell"))
                )
    except TimeoutException:
        logging.error("Did not find header class name in javascript.com site")
    print(driver.title)

def find_java():
    driver.get("http://www.google.com")
    logging.info("This is google.com")
    print(driver.title)
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("java")
    logging.info("typed java into the search bar")
    inputElement.submit()
    try:
        logging.info("Should be clicking the 'Download Free Java Software' search result link.")
        WebDriverWait(driver, 10).until(EC.title_contains("java"))
        print(driver.title)
    except:
        logging.error("No page found.")
    driver.find_element_by_link_text("Download Free Java Software").click()
    try:
        logging.info("We should be in the java.com page now")
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jvh0"))
                )
    except:
        logging.error("Did not find header class name in java.com site")
    print(driver.title)

def find_elixir():
    driver.get("http://www.google.com")
    logging.info("This is google.com")
    print(driver.title)
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("elixir")
    logging.info("typed elixir into the search bar")
    inputElement.submit()
    try:
        logging.info("Should be clicking the 'Elixir' search result link.")
        WebDriverWait(driver, 10).until(EC.title_contains("elixir"))
        print(driver.title)
    except:
        logging.error("No page found.")
    driver.find_element_by_link_text("Elixir").click()
    try:
        logging.info("We should be in the elixir-lang.org page now")
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "branding"))
                )
    except:
        logging.error("Did not find header class name in elixir-lang.org site")
    print(driver.title)

def close():
    driver.close()

find_python()
find_ruby()
find_javascript()
find_java()
find_elixir()
close()

#if __name__ == "__main__":
