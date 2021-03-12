from selenium.webdriver.common.by import By


class MainPageSelectors(object):
    signup_btn = (By.XPATH, '//a[.="Регистрация"]')
    login_input = (By.XPATH, '//input[@data-testid="login-input"]')
    set_pass_btn = (By.XPATH, '//button[@data-testid="enter-password"]')
    login_btn = (By.XPATH, '//button[@data-testid="login-to-mail"]')
    password_input = (By.XPATH, '//input[@data-testid="password-input"]')


class MainPage(object):
    def __init__(self, app):
        self.app = app

    def click_open_signup_form_btn(self):
        self.app.visibility_of_element_located(
            *MainPageSelectors.signup_btn,
            'Не найдена кнопка открытия формы регистрации')
        btn = self.app.wd.find_element(*MainPageSelectors.signup_btn)
        btn.click()

    def set_login(self, login):
        self.app.visibility_of_element_located(*MainPageSelectors.login_input, "Не найдено поле ввода логина")
        login_input = self.app.wd.find_element(*MainPageSelectors.login_input)
        login_input.send_keys(login)

    def click_set_pass_btn(self):
        btn = self.app.wd.find_element(*MainPageSelectors.set_pass_btn)
        btn.click()

    def set_pass(self, password):
        self.app.visibility_of_element_located(*MainPageSelectors.password_input, "Не найдено поле ввода пароля")
        pass_input = self.app.wd.find_element(*MainPageSelectors.password_input)
        pass_input.send_keys(password)

    def click_login_btn(self):
        btn = self.app.wd.find_element(*MainPageSelectors.login_btn)
        btn.click()
