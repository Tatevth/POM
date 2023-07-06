from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from test_data import test_data
import logging
import time


class All_Courses(General_Helper):

    all_courses_btn = (
        By.XPATH, "//div[@id='navbar-inverse-collapse']//a[@href='/courses']")
    search_field = (By.XPATH, "//input[@id='search']")
    search_btn = (
        By.XPATH, "//input[@id='search']//following::button[@type='submit']")
    selenium_courses_titles = (
        By.XPATH, "//div[@id='course-list']//h4[contains(text(),' Selenium ')]")
    selenium_courses_prices = (
        By.XPATH, "//span[@class='zen-course-price dynamic-text']")

    def get_selenium_courses(self):
        try:
            self.find_element_and_send_keys(
                self.search_field, test_data["text"])
            self.find_element_and_click(self.search_btn)
            time.sleep(2)
            titles = self.find_elements(self.selenium_courses_titles)
            prices = self.find_elements(self.selenium_courses_prices)
            logging.info(len(prices))
            selenium_dict = {}
            for title, price in zip(titles, prices):
                selenium_dict[title.text] = price.text
            logging.info("Successfully got the selenium courses.")
            return selenium_dict
        except Exception as e:
            logging.error(e)
