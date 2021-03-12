from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import helpers


class InboxMenuSelectors(object):
    create_new_letter_btn = (By.XPATH, '//a[@title="Написать письмо"]')
    menu_item_with_text = (By.XPATH, '//div[@id="sideBarContent"]//a[contains(@title, "<name>")]')
    expand_letters_block_with_text = (By.XPATH, '//div[contains(@class,"metathread_collapsed")]'
                                                '[contains(.,"Письма себе")]')


class InboxMenu(object):
    def __init__(self, app):
        self.app = app

    def click_create_new_letter_btn(self):
        self.app.visibility_of_element_located(
            *InboxMenuSelectors.create_new_letter_btn,
            "Не найдена кнопка 'Написать письмо'")
        btn = self.app.wd.find_element(*InboxMenuSelectors.create_new_letter_btn)
        btn.click()

    def open_menu_item(self, menu_item):
        menu_item_loc = helpers.get_locator_with_name(InboxMenuSelectors.menu_item_with_text, menu_item)
        self.app.visibility_of_element_located(
            *menu_item_loc,
            f"Не найден пункт меню '{menu_item}'")
        btn = self.app.wd.find_element(*menu_item_loc)
        btn.click()
        self.app.wait.until(EC.url_changes, "Ожидалось, что URL поменяется")

    def expand_letters_block(self, block_text):
        letters_block_loc = helpers.get_locator_with_name(InboxMenuSelectors.expand_letters_block_with_text, block_text)
        self.app.visibility_of_element_located(
            *letters_block_loc,
            f"Не найден блок с письмами {block_text}")
        btn = self.app.wd.find_element(*letters_block_loc)
        btn.click()

