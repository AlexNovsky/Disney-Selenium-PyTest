from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base class for every page object of the web application under test
    Includes all basic page methods, applicable to every page, like (is_displayed,
    click, enter_text, get_title, and many more)
    """

    def __init__(self, driver) -> None:
        self.driver = driver

    """
    Test objects not needed for the 
    """
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    """
    Working objects, not involved in architecture testing starts here
    """
    def is_displayed(self, locator):
        """Check if an element with the provided locator is displayed or not

        :param locator:         2-item tuple containing: (locator strategy, locator identifying string)
        :return:                True if the element is displayed
                                False if the element is hidden or does not exist
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            # return self.driver.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    def open_url(self, url):
        """Open the provided url in a web browser

        :param url:             String, to be typed into the text field
        :return:                None
        """
        self.driver.get(url)

    def click(self, locator):
        """Click action on provided element

        :param locator:         2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        # self.driver.find_element(locator).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def scroll_to(self, locator):
        """Scroll to the provided element. From the nature of this command
            bottom of the element will be at the bottom of the visible part
            of the web page.

        :param locator:         2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        ActionChains(self.driver).scroll_to_element(locator).perform()

    def hover_to(self, locator):
        """Hover over an element with the provided locator

        :param locator:         2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        ActionChains(self.driver).move_to_element(locator).perform()

    def select_item_from_dropdown(self, item_text, dd_locator):
        """Select a drop-down item with the provided text from a drop-down menu with the provided locator

        :param item_text:       String, representing the text contained in a drop-down item in a drop-down menu
                                with the provided dd_locator
        :param dd_locator:      One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        select = Select(dd_locator)
        select.select_by_visible_text(item_text)
    def is_clickable(self, locator):
        """Check if an element with the provided locator is clickable or not

        :param locator:         2-item tuple containing: (locator strategy, locator identifying string)
        :return:                True if the element is displayed
                                False if the element is hidden or does not exist
        """
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.element_to_be_clickable(locator))
        except NoSuchElementException:
            return False

    def get_title(self, title):
        """Return the page title of the currently active browser tab

        :return:                String, representing the page title of the currently active browser tab
        """
        WebDriverWait(self.driver, 5).until(EC.title_is(title))
        return self.driver.title

    def send_keys(self, locator, text):
        """Typing provided text in the provided text field as login forms etc.

        :param locator:         2-item tuple containing: (locator strategy, locator identifying string)
        :param text:            String with the text, which will be sent to the provided text field
        :return:                none
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def clear_field(self, locator):
        field = self.driver.find_element(locator).clear()
