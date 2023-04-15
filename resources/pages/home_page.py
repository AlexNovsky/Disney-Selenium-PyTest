from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from application import Application
from base_page import BasePage

class HomePage(BasePage):
    home_page_url = "https://www.disney.com/"
    sign_in_button = (By.XPATH, '//a[@class="login-link"]')
    home_page_img = (By.XPATH, '//*[@class="disney-img"]')
    home_page_menu = (By.XPATH, '//*[@id="goc-desktop-global"]')
    banner_iframe = (By.CSS_SELECTOR, 'iframe[aria-label="Advertisement"]')
    banner_close_button = (By.XPATH, '//*[@id="overlay"]//*[@class="sprite close"]')

    email = (By.ID, 'username')
    pwd = (By.ID, 'password')
    login_btn = (By.ID, 'loginBtn')
    signup_link = (By.LINK_TEXT, 'Sign up')

    def __init__(self, driver):
        super().__init__(driver)

    '''
    test scenarios for checking architecture workability
    '''
    def get_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.test_send_keys(self.email, username)
        self.test_send_keys(self.pwd, password)
        self.test_click(self.login_btn)



    #
    # driver=webdriver.Chrome()
    #
    #
    # def app(driver):
    #     return Application(driver)
    #
    # def test_closeMainBanner():
    #     wait = WebDriverWait(Application, 5)
    #     wait.until(ex.element_to_be_clickable((self.banner_iframe)))
    #     banner = self.driver.find_element(self.banner_iframe)
    #     if not self.Application.is_displayed(self.banner_close_button):
    #         return False
    #     else:
    #         Application.switch_to.frame(banner)
    #         close_banner = driver.find_element(self.banner_close_button)
    #         close_banner.click()
    #         driver.switch_to.default_content()
    #
    # def test_homePageIsValid():
    #     Application.BasePage.self.is_clickable(home_page_img)
    #     signin_button_text = driver.find_element(By.XPATH, sign_in_button).text
    #     # if not displayed(By.XPATH, home_page_menu) and not displayed(By.XPATH, home_page_img):
    #     #     return False
    #     # if not signin_button_text == 'SIGN IN':
    #     #     return False
    #     # assert signin_button_text == 'SIGN IN'
    #     assert signin_button_text == 'SIGN IN' and driver.title == 'Disney.com | The official home for all things Disney'
    #     assert is_displayed(By.XPATH, home_page_img) != False and is_displayed(By.XPATH, home_page_menu) != False
