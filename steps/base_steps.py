from ..pages.base_page import BasePage


class BaseSteps(object):
    def __init__(self, app):
        self.base_page = BasePage(app)

    def open_page_step(self, link):
        self.base_page.open_page(link)
