from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class SavedPage:
    def __init__(self):
        self.tab_reading_lists = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/nav_tab_reading_lists'))
        self.menu_overflow_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button'))
        self.overflow_create_new_list = browser.element((
            AppiumBy.ID, 'org.wikipedia.alpha:id/reading_lists_overflow_create_new_list'))
        self.button_ok = browser.element((AppiumBy.ID, 'android:id/button1'))

        self.item_title_list = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/item_title'))
        self.count_articles = browser.element((
            AppiumBy.ID, 'org.wikipedia.alpha:id/item_reading_list_statistical_description'))

        self.list = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/recycler_view'))
        self.go_it_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/buttonView'))
        self.item_overflow_menu = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/item_overflow_menu'))

        self.button_edit_name_list = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/content'))
        self.text_input_name = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/text_input'))


    def click_tab_reading_lists(self):
        self.tab_reading_lists.click()

    def click_menu_overflow_button(self):
        self.menu_overflow_button.click()

    def click_overflow_create_new_list(self):
        self.overflow_create_new_list.click()

    def click_button_ok(self):
        self.button_ok.click()

    def should_be_visible_new_list(self):
        self.item_title_list.should(have.exact_text('My reading list'))

    def should_be_visible_count_articles(self):
        self.count_articles.should(have.exact_text('0 articles'))

    def create_new_list(self):
        self.click_tab_reading_lists()
        self.click_menu_overflow_button()
        self.click_overflow_create_new_list()
        self.click_button_ok()

    def open_list(self):
        self.list.click()
        self.go_it_button.click()

    def edit_name_list(self):
        self.open_list()
        self.item_overflow_menu.click()
        self.button_edit_name_list.click()
        self.text_input_name.type('Change name')
        self.click_button_ok()

    def should_be_change_name(self):
        self.item_title_list.should(have.exact_text('Change name'))

