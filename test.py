from Lib.driver_lib import Driver_Lib
from Lib.general_lib import General_Helper
from Page.main_page import Main_Page
from Page.login import Login_Page
from Page.all_courses import All_Courses
import logging


def test():
    driver_lib = Driver_Lib()
    driver = driver_lib.get_driver()
    main_page = Main_Page(driver)
    login_page = Login_Page(driver)
    all_courses = All_Courses(driver)

    main_page.open_page()
    login_page.login()
    all_courses.find_element_and_click(all_courses.all_courses_btn)
    try:
        title_price_dict = all_courses.get_selenium_courses()
        logging.info(f"The titles and prices: {title_price_dict}")
    finally:
        driver_lib.quit_driver()
        logging.info("Driver is closed.")


if __name__ == "__main__":
    test()
