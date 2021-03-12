from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Application(object):

    def __init__(self, browser, timeout, base_url):
        browser_variants = ['chrome', 'firefox']
        if browser not in browser_variants:
            assert False, F"Предоставлено неизвестное название браузера: '{browser}'. " \
                          F"Возможные варианты: {browser_variants}"
        if 'chrome' in browser:
            self.wd = webdriver.Chrome(ChromeDriverManager().install())
        if 'firefox' in browser:
            self.wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        if type(timeout) == int and timeout >= 0:
            self.wd.implicitly_wait(timeout)
        else:
            assert False, F"Предоставлен некорректный таймаут для браузера: '{timeout}'"
        self.wd.implicitly_wait(timeout)
        self.wait = WebDriverWait(self.wd, timeout)
        self.timeout = timeout
        self.base_url = base_url

    def visibility_of_element_located(self, strategy, locator, message, timeout=10):
        WebDriverWait(self.wd, timeout).until(
            EC.visibility_of_element_located((strategy, locator)),
            F"За {timeout} сек:{message}"
        )

    def invisibility_of_element_located(self, strategy, locator, message, timeout=10):
        self.wd.implicitly_wait(0)
        WebDriverWait(self.wd, timeout).until(
            EC.invisibility_of_element_located((strategy, locator,)),
            F"За {timeout} сек:{message}"
        )
