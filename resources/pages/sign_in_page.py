from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.common.by import By
from .base_page import BasePage


class SignInPage(BasePage):
    valid_email = 'pythonminutes@gmail.com'
    valid_pwd = 'pythonMinutes1'

    log_in_iframe = (By.XPATH, 'iframe[id="oneid-iframe"]')
    sign_in_button = (By.XPATH, '//a[@class="login-link"]')
    disney_account_img = (By.XPATH, '//*[@id="logo"]')  # text: 'Disney account'
    enter_email_sign = (By.XPATH, '//*[@id="Title"]')  # //*[contains(text(), "Enter Your Email Address")]' #text: 'Enter Your Email Address'
    enter_email_textbox = (By.XPATH, '//*[@class="input-InputIdentityFlowValue"]')
    submit_email_btn = '//button[@data-testid="BtnSubmit"]'  # text: 'Continue'
    enter_pwd_sign = '//*[@id="Title"]'  # //*[contains(text(), "Enter Your Password")]' #text: 'Enter Your Password'
    login_email_value = '//*[@id="InputLoginValue"]'
    enter_pwd_textbox = '//*[@class="input-InputPassword"]'
    forgot_pwd_btn = '//*[@id="HelpSigningIn"]'  # text: 'Forgot your password?'
    submit_pwd_btn = '//button[@data-testid="BtnSubmit"]'  # text: 'Sign In'
    invalid_email = '//*[@id="InputIdentityFlowValue-error"]'  # //*[contains(text(), "Please enter a valid email address")]
    invalid_pwd = '//*[@id="LoginError"]'  # text: The credentials you entered are incorrect.
    logged_in = '//*[@id="goc-user"]//*[@class="goc-login"]//a'  # '//*[@id="goc-user"]' #text: My Account
    my_account_btn = '//*[@id="goc-user"]//a[@class="login-dropdown-title-link"]'  # text: My Account
    account_settings_btn = '//a[@class="login-dropdown-link dropdown_link"]'  # //u[contains(text(),"Account Settings")]' #text: Account Settings
    sign_out_btn = '//*[@id="goc-user"]//a[@class="login-dropdown-link"]//u'  # text: Sign Out

    def signInIsLoaded(self) -> bool:
        """
        Chec if sign-in menu is loaded and click Sign-In button
        :return:        True if frame is displayed
                        False if frame is hidden ot not exist
        """
        self.is_clickable(self.sign_in_button)
        if not self.is_clickable(self.sign_in_button):
            return False
        self.click(self.sign_in_button)

    def signInFrameIsDisplayed(self) -> bool:
        """
        Check if Sign-In frame is shown (popped up) or not with required elements
        :return:        True if frame is displayed and elements are visible
                        False if frame not displayed or required elements not visible
        """
        wait = WebDriverWait(self.driver, 5)
        wait.until(ex.presence_of_element_located(self.log_in_iframe))
        if not self.is_displayed(self.log_in_iframe):
            return False
        loginframe = self.driver.find_element(self.log_in_iframe)
        self.switch_to.frame(loginframe)
        if not self.is_displayed(self.disney_account_img):
            return False
        if not self.is_displayed(self.enter_email_sign):
            return False

    def enterValidEmail(self):
        """
        Enter the e-mail from variable. Before sending keys, clear the textbox
        :return:        None
        """
        self.click(self.enter_email_textbox)
        self.clear_field(self.enter_email_textbox)
        self.send_keys(self.enter_email_textbox, self.valid_email)
        self.click(self.submit_email_btn)

    def signInPwdIsLoaded(self) -> bool:
        """
        Check if enter password frame is shown (popped up) or not with required elements
        :return:        True if frame is displayed and elements are visible
                        False if frame not displayed or required elements not visible
        """
        wait = WebDriverWait(self.driver, 5)
        wait.until(ex.presence_of_element_located(self.enter_pwd_sign))
        if not self.is_displayed(self.enter_pwd_sign):
            return False

    def enterValidPwd(self):
        """
        Enter password from variable. Before sending keys, clear the textbox
        :return:        None
        """
        self.click(self.enter_pwd_textbox)
        self.clear_field(self.enter_pwd_textbox)
        self.send_keys(self.enter_pwd_textbox, self.valid_pwd)
        self.click(self.submit_pwd_btn)
        self.switch_to.default_content()

    def signedInIsLoaded(self) -> bool:
        """
        Check if user signed in successfully  or not with required elements
        :return:        True if user logged in
                        False if user not logged in
        """
        if not self.is_displayed(self.logged_in):
            return False

    def signOut(self):
        self.is_clickable(self.my_account_btn)
        if not self.is_clickable(self.my_account_btn):
            return False
        self.click(self.my_account_btn)
        self.is_clickable(self.sign_out_btn)
        if not self.is_clickable(self.sign_out_btn):
            return False
        self.click(self.sign_out_btn)
