from selene import be, have


def test_noneempty_search_result(google_page, random_string):
    browser = google_page
    browser.element('[type="search"]').should(be.blank).type('github').press_enter()
    browser.element('[id="res"]').should(have.text("GitHub: Let's build from here · GitHub"))


def test_empty_search_result(google_page, random_string):
    browser = google_page
    browser.element('[type="search"]').should(be.blank).type(random_string).press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
