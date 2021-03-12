import pytest
from .application import Application


# noinspection SpellCheckingInspection
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--timeout", action="store", default="10", help="Implicitly wait timeout delay")
    parser.addoption("--server", action="store", default="prod", help="Server to run tests")


@pytest.fixture(autouse=True)
def app(request):
    browser = request.config.getoption("browser")
    timeout_delay = int(request.config.getoption("timeout"))
    server = request.config.getoption("server")
    base_url = ""
    if server == "prod":
        base_url = "https://mail.ru/"
    app = Application(browser, timeout_delay, base_url)
    yield app
    app.wd.quit()
