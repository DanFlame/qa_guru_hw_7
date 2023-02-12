import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def open_browser_with_max_size():
    browser.open('https://google.com')
    browser.driver.fullscreen_window()
