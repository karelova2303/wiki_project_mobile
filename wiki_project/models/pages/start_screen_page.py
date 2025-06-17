from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class StartScreenPage:
    def __init__(self):
        self.primary_text_view = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        self.forward_button = browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
        self.done_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button'))
        self.main_toolbar = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark'))

    def should_have_text_on_the_screen(self, value):
        self.primary_text_view.should(have.text(value))

    def click_forward_button(self):
        self.forward_button.click()

    def click_done_button(self):
        self.done_button.click()

    def should_be_visible_main_page(self):
        self.main_toolbar.should(be.visible)
