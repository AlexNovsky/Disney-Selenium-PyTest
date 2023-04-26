import pytest
from resources.pages.application import Application


@pytest.mark.home_page
class TestHomePage:
    def test_home_page_is_displayed(self, app):
        assert Application.openHomePage() == 'Disney.com | The official home for all things Disney'

    def test_home_page_elements(self, app):
        assert not Application.homePageElementsInPlace() != True

    def test_banner_is_displayed(self, app):
        assert not Application.isBannerDisplayed() != True

    def test_banner_is_closed(self, app):
        assert not Application.bannerClose() != True
