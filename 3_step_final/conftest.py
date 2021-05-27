import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    if browser_lang == "es":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_lang == "ru":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_lang == "fr":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_lang should be language or language not found")

    yield browser
    print("\nquit browser..")
    browser.quit()