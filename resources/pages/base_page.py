from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

# class BasePage:
#     """Base class for every page object of the web application under test
#     Includes all basic page methods, applicable to every page, like (get_element,
#     is_displayed, click, enter_text, get_element_text, and many more)
#     Requires app_data dictionary (containing WebDriver, test data, and other settings) as an input
#     """
#
driver = webdriver.Chrome()


def is_displayed(by, locator):
    try:
        return driver.find_element(By.XPATH, locator).is_displayed()
        # return self.driver.find_element(by, locator).is_displayed()
    except NoSuchElementException:
        return False
