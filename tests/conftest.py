import pytest
from selenium import webdriver
from resources.pages.application import Application


@pytest.fixture(scope='session')
def app():
    web_driver = webdriver.Chrome()
    app = Application(web_driver)
    yield app
    web_driver.close()
