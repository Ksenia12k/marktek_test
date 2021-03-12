from ..pages.signup_page import SignupPage
import helpers


class SignupSteps(object):
    def __init__(self, app):
        self.app = app
        self.signup_page = SignupPage(app)

    def fill_in_signup_form_step(self, name, last_name, gender, email, password):
        email_id = helpers.get_random_number(10000000, 1000000000)
        self.signup_page.write_in_input("fname", name)
        self.signup_page.write_in_input("lname", last_name)
        self.signup_page.set_birthday()
        self.signup_page.set_gender(gender)
        self.signup_page.write_in_input("username", email+str(email_id))
        self.signup_page.write_in_input("password", password)
        self.signup_page.write_in_input("repeatPassword", password)
        self.signup_page.click_create_btn()
