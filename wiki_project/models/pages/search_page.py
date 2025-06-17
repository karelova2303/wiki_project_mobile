from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchPage:
    def __init__(self):
        self.skip_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button'))
        self.search_text = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia'))
        self.search_src_text = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text'))

        self.all_page_list_item_title = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        self.page_list_item_title = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))

    def skip_start_screen(self):
        self.skip_button.click()

    def input_text_in_search(self, value):
        self.search_text.click()
        self.search_src_text.type(value)

    def should_have_text_title(self, value):
        self.all_page_list_item_title.should(have.size_greater_than(0))
        self.all_page_list_item_title.first.should(have.text(value))

    def should_be_clickable_title(self):
        self.page_list_item_title.click()
