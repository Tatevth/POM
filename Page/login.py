from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from config import config_data
import logging
from selenium.webdriver.support import expected_conditions


class Login_Page(General_Helper):

    login_page = (By.XPATH, "//a[@href='/login']")
    email_field = (By.XPATH, "//input[@id='email']")
    pass_field = (By.XPATH, "//input[@id='login-password']")
    login_btn = (By.XPATH, "//button[@id='login']")
    my_acc_dropdown = (By.XPATH, "//button[@id='dropdownMenu1']")

    def login(self):
        try:
            self.find_element_and_click(self.login_page)
            self.find_element_and_send_keys(
                self.email_field, config_data["email"])
            self.find_element_and_send_keys(
                self.pass_field, config_data["password"])
            self.find_element_and_click(self.login_btn)
            element_present = expected_conditions.presence_of_element_located(
                self.my_acc_dropdown)
            if element_present:
                logging.info("Successfully logged in.")
            else:
                logging.error("Couldn't logged in.")
        except Exception as e:
            logging.error(e)
