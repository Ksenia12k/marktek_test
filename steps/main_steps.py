from ..pages.main_page import MainPage


class MainSteps(object):
    def __init__(self, app):
        self.main_page = MainPage(app)

    def open_signup_form_step(self):
        self.main_page.click_open_signup_form_btn()

    def login_step(self, login, password):
        self.main_page.set_login(login)
        self.main_page.click_set_pass_btn()
        self.main_page.set_pass(password)
        self.main_page.click_login_btn()
