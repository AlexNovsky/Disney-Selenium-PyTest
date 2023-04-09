import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from resources.pages.base_page import is_displayed
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

home_page_url = "https://www.disney.com/"
sign_in_button = '//a[@class="login-link"]'
home_page_img = '//*[@class="disney-img"]'
home_page_menu = '//*[@id="goc-desktop-global"]'
banner_iframe = 'iframe[aria-label="Advertisement"]'
banner_close_button = '//*[@id="overlay"]//*[@class="sprite close"]'

driver = webdriver.Chrome()


@pytest.mark.homepage_valid
def test_homePageIsValid():
    driver.get(home_page_url)
    signin_button_text = driver.find_element(By.XPATH, sign_in_button).text
    if not is_displayed(By.XPATH, home_page_menu) and not is_displayed(By.XPATH, home_page_img):
        # print('Home page not loaded')
        return False
    # print('Home page is displayed')
    if not signin_button_text == 'SIGN IN':
        return False
    assert signin_button_text == 'SIGN IN'


def test_closeMainBanner():
    wait = WebDriverWait(driver, 5)
    wait.until(ex.element_to_be_clickable((By.CSS_SELECTOR, banner_iframe)))
    banner = driver.find_element(By.CSS_SELECTOR, banner_iframe)
    driver.switch_to.frame(banner)
    close_banner = driver.find_element(By.XPATH, banner_close_button)
    close_banner.click()
    driver.switch_to.default_content()
