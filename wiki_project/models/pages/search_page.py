from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchPage:
    def __init__(self):
        self.locator_url = 'org.wikipedia.alpha:id'

        self.skip_button = browser.element((AppiumBy.ID, f'{self.locator_url}/fragment_onboarding_skip_button'))
        self.search_text = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia'))
        self.search_src_text = browser.element((AppiumBy.ID, f'{self.locator_url}/search_src_text'))

        self.all_page_list_item_title = browser.all((AppiumBy.ID, f'{self.locator_url}/page_list_item_title'))
        self.page_list_item_title = browser.element((AppiumBy.ID, f'{self.locator_url}/page_list_item_title'))

    def skip_start_screen(self):
        with step('Пропускаем экран приветствия'):
            self.skip_button.click()

    def input_text_in_search(self, value):
        with step('Вводим текст в строку поиска'):
            self.search_text.click()
            self.search_src_text.type(value)

    def title_should_have_text(self, value):
        with step('Проверяем найденный контент'):
            self.all_page_list_item_title.should(have.size_greater_than(0))
            self.all_page_list_item_title.first.should(have.text(value))

    def title_should_be_clickable(self):
        with step('Проверяем, что найденный контент кликабельный'):
            self.page_list_item_title.click()
