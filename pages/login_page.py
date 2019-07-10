from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "It isn't login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        login_field.send_keys(email)

        pass_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD)
        pass_field.send_keys(password)
        pass_confirm_field = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD)
        pass_confirm_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
