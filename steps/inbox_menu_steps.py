from ..components.inbox_menu import InboxMenu


class InboxMenuSteps(object):
    def __init__(self, app):
        self.inbox_menu = InboxMenu(app)

    def click_create_new_letter_btn_step(self):
        self.inbox_menu.click_create_new_letter_btn()

    def open_menu_item_step(self, menu_item):
        self.inbox_menu.open_menu_item(menu_item)

    def expand_letters_block_step(self, block_text):
        self.inbox_menu.expand_letters_block(block_text)
