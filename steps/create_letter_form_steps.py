from ..components.create_letter_form import CreateLetterForm
import helpers


class CreateLetterFormSteps(object):
    def __init__(self, app):
        self.app = app
        self.create_letter_form = CreateLetterForm(app)

    def send_letter_step(self, recipient, text):
        letter_text = text + str(helpers.get_random_number(10000000, 1000000000))
        self.create_letter_form.set_recipient(recipient)
        self.create_letter_form.set_letter_text(letter_text)
        self.create_letter_form.click_send_letter_btn()
        return letter_text

    def check_letter_sent_popup_step(self):
        self.create_letter_form.check_letter_sent_popup()
        self.create_letter_form.close_letter_sent_popup()
