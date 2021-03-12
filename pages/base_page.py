class BasePage(object):
    def __init__(self, app):
        self.app = app

    def open_page(self, link):
        self.app.wd.get(link)

