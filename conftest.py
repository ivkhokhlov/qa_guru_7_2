import string
from random import shuffle

import pytest
from selene import browser


@pytest.fixture(scope='session')
def firefox_browser():
    browser.config.driver_name = 'firefox'
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
