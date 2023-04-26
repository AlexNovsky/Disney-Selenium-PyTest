from .base_page import BasePage
from .home_page import HomePage


class Application:
    """Returns an object, containing all the Page Objects of the web application under test.

    Includes BasePage with all its standard methods (get_element, is_displayed, click, etc.)
    and all the child page objects (HomePage etc.) with all their locators (header, search_bar,
    product_name, footer, etc.)
    """

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.home_page = HomePage(driver)
