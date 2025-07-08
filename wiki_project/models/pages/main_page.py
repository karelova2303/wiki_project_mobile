from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class MainPage:
    def __init__(self):
        self.locator_url = 'org.wikipedia.alpha:id'

        self.primary_text_view = browser.element((AppiumBy.ID, f'{self.locator_url}/primaryTextView'))
        self.forward_button = browser.element((AppiumBy.ID, f'{self.locator_url}/fragment_onboarding_forward_button'))
        self.done_button = browser.element((AppiumBy.ID, f'{self.locator_url}/fragment_onboarding_done_button'))
        self.main_toolbar = browser.element((AppiumBy.ID, f'{self.locator_url}/main_toolbar_wordmark'))

    def should_have_text_on_the_screen(self, value):
        with step(f'Проверка, что отобразился текст'):
            self.primary_text_view.should(have.text(value))

    def click_forward_button(self):
        with step('Кликнуть кнопку "Continue"'):
                self.forward_button.click()

    def click_done_button(self):
        with step('Кликнуть кнопку "Get started"'):
            self.done_button.click()

    def main_page_appears(self):
        with step('Проверка, что отобразился тулбар'):
            self.main_toolbar.should(be.visible)
