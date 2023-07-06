from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class General_Helper:

    def __init__(self, driver):
        self.driver = driver
        logging.basicConfig(filename='test.log', format='%(filename)s: %(message)s',
                    level=logging.INFO)

    def find_element(self, loc, timeout=60):
        try:
            element = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(loc))
            return element
        except Exception as e:
            logging.error("Element isn't found!")

    def find_elements(self, loc, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout=timeout).until(
                EC.visibility_of_all_elements_located(loc))
            return elements
        except Exception as e:
            logging.error("Elements aren't found! Error: %s" % e)

    def find_element_and_click(self, loc, timeout=60):
        try:
            element = WebDriverWait(self.driver, timeout=timeout).until(
                EC.element_to_be_clickable(loc))
            element.click()
            logging.info("The element is clickable.")
        except:
            logging.error("Couldn't click on the element.")
    
    def find_element_and_send_keys(self,loc,text,timeout=60):
        element = self.find_element(loc)
        try:
            element.send_keys(text)
            logging.info(f"The- {text}, is put in the field.")
        except:
            logging.error(f"Couldn't put the- {text}, in the field")
            
    def find_element_text(self,loc,timeout = 60):
        element = self.find_element(loc)
        return element.text
    