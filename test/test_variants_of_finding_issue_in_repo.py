import allure
from allure_commons.types import Severity
from selene.support.conditions import be
from selene.support import by
from selene.support.shared import browser


# 1. Чистый селен
@allure.tag('WEB')
@allure.label('owner', 'danflame')
@allure.severity(Severity.CRITICAL)
@allure.feature('Issues list in repository')
@allure.description('We should check that issues are visible')
@allure.story('Finding issue with special name for this pure selene test')
@allure.link('https://github.com/DanFlame/qa_guru_hw_7/tree/main/test', name='Test directory')
def test_github_issue_finding_with_selene():
    browser.open('https://github.com/')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('danflame/qa_guru_hw_6')
    browser.element('.header-search-input').press_enter()
    browser.element(by.link_text('DanFlame/qa_guru_hw_6')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('selene')).should(be.visible)


# 2. Лямбда шаги
@allure.tag('WEB')
@allure.label('owner', 'danflame')
@allure.severity(Severity.CRITICAL)
@allure.feature('Issues list in repository')
@allure.description('We should check that issues are visible')
@allure.story('Finding issue with special name for this test with lambda steps')
@allure.link('https://github.com/DanFlame/qa_guru_hw_7/tree/main/test', name='Test directory')
def test_github_issue_finding_with_lambda_steps():
    with allure.step('Open Github main page'):
        browser.open('https://github.com/')

    with allure.step('Click the search input'):
        browser.element('.header-search-input').click()

    with allure.step('Type directory path'):
        browser.element('.header-search-input').type('danflame/qa_guru_hw_6')

    with allure.step('Confirm search request'):
        browser.element('.header-search-input').press_enter()

    with allure.step('Click the repo'):
        browser.element(by.link_text('DanFlame/qa_guru_hw_6')).click()

    with allure.step('Choose issues tab'):
        browser.element('#issues-tab').click()

    with allure.step('Check for required issue'):
        browser.element(by.partial_text('lambda')).should(be.visible)


# 3. Декоратор
@allure.tag('WEB')
@allure.label('owner', 'danflame')
@allure.severity(Severity.CRITICAL)
@allure.feature('Issues list in repository')
@allure.description('We should check that issues are visible')
@allure.story('Finding issue with special name for this test with decorator')
@allure.link('https://github.com/DanFlame/qa_guru_hw_7/tree/main/test', name='Test directory')
def test_github_issue_finding_with_decorator():
    open_main_github_page()
    search_input_click()
    directory_path_type('danflame/qa_guru_hw_6')
    confirm_search_request()
    go_to_repository('DanFlame/qa_guru_hw_6')
    open_issues_tab()
    is_issue_visible('decorator')


@allure.step('Open Github main page')
def open_main_github_page():
    browser.open('https://github.com/')


@allure.step('Click the search input')
def search_input_click():
    browser.element('.header-search-input').click()


@allure.step('Type directory path')
def directory_path_type(directory_path):
    browser.element('.header-search-input').type(directory_path)


@allure.step('Confirm search request')
def confirm_search_request():
    browser.element('.header-search-input').press_enter()


@allure.step('Click the repo')
def go_to_repository(repository_path):
    browser.element(by.link_text(repository_path)).click()


@allure.step('Choose issues tab')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Check for required issue')
def is_issue_visible(part_of_issue_title):
    browser.element(by.partial_text(part_of_issue_title)).should(be.visible)
