from ..pages.captcha_page import CaptchaPage


class CaptchaSteps(object):
    def __init__(self, app):
        self.main_page = CaptchaPage(app)

    def check_captcha_is_visible_step(self):
        self.main_page.check_captcha_is_visible()
