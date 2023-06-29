import pytest
from resources.disney.pages.application import Application


@pytest.mark.home_page
class TestHomePage:
    def test_home_page_is_displayed(self, app):
        assert app.home_page.openHomePage(self) == 'Disney.com | The official home for all things Disney'

    def test_home_page_elements(self, app):
        assert not app.home_page.homePageElementsInPlace() != True

    def test_banner_is_displayed(self, app):
        assert not app.home_page.isBannerDisplayed() != True

    def test_banner_is_closed(self, app):
        assert not app.home_page.bannerClose() != True
