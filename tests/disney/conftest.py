import pytest
# import sys
# from os import path
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from selenium import webdriver
from resources.disney.pages.application import Application
from resources.disney.pages.home_page import HomePage


@pytest.fixture(scope='session')
def app():
    web_driver = webdriver.Chrome()
    app = Application(web_driver)
    app.home_page = HomePage
    yield app
    web_driver.close()
