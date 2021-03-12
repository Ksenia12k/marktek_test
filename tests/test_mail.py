from ..steps.create_letter_form_steps import CreateLetterFormSteps
from ..steps.letters_list_steps import LettersListSteps
from ..steps.inbox_menu_steps import InboxMenuSteps
from ..steps.captcha_steps import CaptchaSteps
from ..steps.base_steps import BaseSteps
from ..steps.main_steps import MainSteps
from ..steps.signup_steps import SignupSteps


def test_create_new_mail_user(app):
    base_steps = BaseSteps(app)
    main_steps = MainSteps(app)
    signup_steps = SignupSteps(app)
    captcha_steps = CaptchaSteps(app)

    base_steps.open_page_step(app.base_url)
    main_steps.open_signup_form_step()
    signup_steps.fill_in_signup_form_step("TestName", "TestLastName", "Male", "testEmail", "krYojtEU31I|")
    captcha_steps.check_captcha_is_visible_step()


def test_send_email(app):
    base_steps = BaseSteps(app)
    main_steps = MainSteps(app)
    inbox_menu_steps = InboxMenuSteps(app)
    create_letter_form_steps = CreateLetterFormSteps(app)
    letters_list_steps = LettersListSteps(app)

    base_steps.open_page_step(app.base_url)
    main_steps.login_step("test_marktek", "&ryPTPenrO24")
    inbox_menu_steps.click_create_new_letter_btn_step()
    letter_text = create_letter_form_steps.send_letter_step("test_marktek@mail.ru", "Test")
    create_letter_form_steps.check_letter_sent_popup_step()
    inbox_menu_steps.open_menu_item_step("Входящие")
    inbox_menu_steps.expand_letters_block_step("Письма себе")
    letters_list_steps.check_new_letter_is_in_list_step(letter_text)




