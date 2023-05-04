from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from .base_page import BasePage


class HomePage(BasePage):
    home_page_url = "https://www.disney.com/"
    sign_in_button = (By.XPATH, '//a[@class="login-link"]')
    home_page_img = (By.XPATH, '//*[@class="disney-img"]')
    home_page_menu = (By.XPATH, '//*[@id="goc-desktop-global"]')
    banner_iframe = (By.CSS_SELECTOR, 'iframe[aria-label="Advertisement"]')
    banner_close_button = (By.XPATH, '//*[@id="overlay"]//*[@class="sprite close"]')

    def openHomePage(self):
        """
        Open the provided URL and returning webpage title
        :return: str. Opened webpage title
        """
        self.open_url(self.home_page_url)
        return self.get_title(self)

    def homePageElementsInPlace(self) -> bool:
        """
        Checking if all required elements of the page are displayed
        :return:        True if the elements are displayed
                        False if the elements are hidden ot not exist
        """
        self.is_clickable(self.home_page_img)
        signin_button_text = self.driver.find_element(self.sign_in_button).text
        if not signin_button_text == 'SIGN IN':
            return False
        elif not self.is_displayed(self.home_page_img) == True and\
                not self.is_displayed(self.home_page_menu) == True:
            return False
        else:
            return True

    def isBannerDisplayed(self) -> bool:
        """
        Check if advertisement banner is shown (popped up) or not
        :return:        True if banner is displayed
                        False if banner not displayed
        """
        wait = WebDriverWait(self.driver, 5)
        wait.until(ex.element_to_be_clickable(self.banner_iframe))
        if not self.is_displayed(self.banner_close_button):
            return False

    def bannerClose(self) -> bool:
        """
        Closes advertisement banner on the home page
        :return:        True if banner is closed and  focus return to default content (the web page itself)
                        False if banner still on the screen
        """
        banner = self.driver.find_element(self.banner_iframe)
        self.switch_to.frame(banner)
        self.click(self.banner_close_button)
        if not self.is_displayed(self.banner_close_button):
            self.driver.switch_to.default_content()
            return True
