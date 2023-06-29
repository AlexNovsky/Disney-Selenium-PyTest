import pytest
from resources.disney.pages.application import Application


@pytest.mark.signin_page
class TestSignInPage:
    def test_signin_is_loaded(self, app):
        assert not Application.signInIsLoaded() != True

    def test_signin_frame_visible(self, app):
        assert not Application.signInFrameIsDisplayed() != True

    def test_enter_email(self, app):
        Application.enterValidEmail()

    def test_password_textbox_loaded(self, app):
        assert not Application.signInPwdIsLoaded() != True

    def test_enter_password(self, app):
        Application.enterValidPwd()

    def test_user_signed_in(self, app):
        assert not Application.signedInIsLoaded() != True

    def test_user_signed_out(self, app):
        assert not Application.signOut() != True
