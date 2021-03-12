from selenium.webdriver.common.by import By
import random


class CaptchaPageSelectors(object):
    captcha_form = (By.XPATH, '//form[@data-test-id="signup-verification-step"]')


class CaptchaPage(object):
    def __init__(self, app):
        self.app = app

    def check_captcha_is_visible(self):
        self.app.visibility_of_element_located(
            *CaptchaPageSelectors.captcha_form,
            f'Не найдена форма капчи')
