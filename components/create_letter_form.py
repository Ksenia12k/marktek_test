from selenium.webdriver.common.by import By


class CreateLetterFormSelectors(object):
    recipient_input = (By.XPATH, '//div[contains(@class, "contactsContainer--")]//input')
    letter_textbox = (By.XPATH, '//div[@role="textbox"]')
    send_letter_btn = (By.XPATH, '//span[@title="Отправить"]')
    confirm_sent_letter_popup = (By.XPATH, '//div[contains(@class,"layer-sent-page")]')
    close_confirm_sent_letter_popup_btn = (By.XPATH, '//span[@title="Закрыть"]')


class CreateLetterForm(object):
    def __init__(self, app):
        self.app = app

    def set_recipient(self, recipient):
        self.app.visibility_of_element_located(
            *CreateLetterFormSelectors.recipient_input,
            "Не найдено поле ввода получателя"
        )
        recipient_input = self.app.wd.find_element(*CreateLetterFormSelectors.recipient_input)
        recipient_input.send_keys(recipient)

    def set_letter_text(self, text):
        self.app.visibility_of_element_located(
            *CreateLetterFormSelectors.recipient_input,
            "Не найдено поле ввода текста сообщения"
        )
        recipient_input = self.app.wd.find_element(*CreateLetterFormSelectors.letter_textbox)
        recipient_input.send_keys(text)

    def click_send_letter_btn(self):
        btn = self.app.wd.find_element(*CreateLetterFormSelectors.send_letter_btn)
        btn.click()
        self.app.invisibility_of_element_located(
            *CreateLetterFormSelectors.send_letter_btn,
            "Ожидалось, что после нажания на кнопку отправки сообщения, она пропадет"
        )

    def check_letter_sent_popup(self):
        self.app.visibility_of_element_located(
            *CreateLetterFormSelectors.confirm_sent_letter_popup,
            "Не найдено всплывающее окно с подтверждением отправки письма"
        )

    def close_letter_sent_popup(self):
        btn = self.app.wd.find_element(*CreateLetterFormSelectors.close_confirm_sent_letter_popup_btn)
        btn.click()
        self.app.invisibility_of_element_located(
            *CreateLetterFormSelectors.send_letter_btn,
            "Ожидалось, что после нажания на кнопку отправки сообщения, она пропадет"
        )




