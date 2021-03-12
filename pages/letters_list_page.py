from selenium.webdriver.common.by import By
import helpers


class LetterListPageSelectors(object):
    letter_with_text = (By.XPATH, '//div[@class="llc__content"]//span[@class="ll-sp__normal"][contains(.,"<name>")]')


class LettersListPage(object):
    def __init__(self, app):
        self.app = app

    def check_new_letter_is_in_list(self, letter_text):
        letter_with_text_loc = helpers.get_locator_with_name(LetterListPageSelectors.letter_with_text, letter_text)
        self.app.visibility_of_element_located(
            *letter_with_text_loc,
            f"Не найдено письмо с текстом {letter_text}")

