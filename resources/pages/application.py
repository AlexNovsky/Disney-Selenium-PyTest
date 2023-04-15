from base_page import BasePage
from home_page import HomePage


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.home_page = HomePage(driver)
