from selenium.webdriver.common.by import By
import random
import helpers


class SignupPageSelectors(object):
    input_with_name = (By.XPATH, '//input[@name="<name>"]')
    birthday_selects = (By.XPATH, '//div[contains(@data-test-id, "birth-date__")]')
    select_value = (By.XPATH, '//div[contains(@data-test-id, "select-value")]')
    select_values_block = (By.XPATH, '//div[@data-test-id="select-menu-wrapper"]'
                                     '//div[contains(@data-test-id,"birth-date__")]')
    gender_label_with_name = (By.XPATH, '//label[@data-test-id="gender-<name>"]')
    create_btn = (By.XPATH, '//button[@data-test-id="first-step-submit"]')


class SignupPage(object):
    def __init__(self, app):
        self.app = app

    def write_in_input(self, input_name, text):
        phone_input_loc = helpers.get_locator_with_name(SignupPageSelectors.input_with_name, input_name)
        phone_input = self.app.wd.find_element(*phone_input_loc)
        phone_input.send_keys(text)

    def set_birthday(self):
        self.app.visibility_of_element_located(
                *SignupPageSelectors.birthday_selects,
                f'Не найдено поле выбора дня рождения в форме')
        selects = self.app.wd.find_elements(*SignupPageSelectors.birthday_selects)
        for select in selects:
            select.click()
            self.app.visibility_of_element_located(
                *SignupPageSelectors.select_values_block,
                f'Не найдены варианты в выпадающем списке даты рождения')
            select_values_list = self.app.wd.find_elements(*SignupPageSelectors.select_value)
            if "year" in select.get_attribute("data-test-id"):
                select_values_list.pop(0)
            select_value = random.choice(select_values_list)
            select_value.click()

    def set_gender(self, gender):
        gender = gender.lower()
        label_loc = helpers.get_locator_with_name(SignupPageSelectors.gender_label_with_name, gender)
        label = self.app.wd.find_element(*label_loc)
        label.click()

    def click_create_btn(self):
        create_btn = self.app.wd.find_element(*SignupPageSelectors.create_btn)
        create_btn.click()



