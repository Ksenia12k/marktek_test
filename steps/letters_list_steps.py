from ..pages.letters_list_page import LettersListPage
import time


class LettersListSteps(object):
    def __init__(self, app):
        self.app = app
        self.letters_list_page = LettersListPage(app)

    def check_new_letter_is_in_list_step(self, letter_text):
        self.letters_list_page.check_new_letter_is_in_list(letter_text)
