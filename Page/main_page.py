from Lib.general_lib import General_Helper
from config import config_data
import logging


class Main_Page(General_Helper):

    def open_page(self):
        self.driver.get(config_data["url"])
        logging.info("The page is successfully opened.")
