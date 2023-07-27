import string
from random import shuffle

import pytest
from selene import browser
from selene.core.configuration import Config


@pytest.fixture(scope='session')
def firefox_browser():
    browser.config.driver_name = 'firefox'
    Config.window_width = 1920
    Config.window_height = 1080
    yield browser
    browser.quit()


@pytest.fixture
def google_page(firefox_browser):
    browser.open('https://www.google.com/')
    return browser


@pytest.fixture
def random_string():
    letters = list(string.ascii_letters)
    shuffle(letters)
    return ''.join(letters)
