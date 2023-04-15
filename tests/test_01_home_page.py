import pytest
from resources.pages.application import Application


class test_homePage(Application):
    def app(driver):
        return Application(driver)

    def test_login(self):
