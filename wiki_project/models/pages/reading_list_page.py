from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class SavedPage:
    def __init__(self):
        self.locator_url = 'org.wikipedia.alpha:id'

        self.tab_reading_lists = browser.element((AppiumBy.ID, f'{self.locator_url}/nav_tab_reading_lists'))
        self.menu_overflow_button = browser.element((AppiumBy.ID, f'{self.locator_url}/menu_overflow_button'))
        self.overflow_create_new_list = browser.element((
            AppiumBy.ID, f'{self.locator_url}/reading_lists_overflow_create_new_list'))
        self.button_ok = browser.element((AppiumBy.ID, 'android:id/button1'))

        self.item_title_list = browser.element((AppiumBy.ID, f'{self.locator_url}/item_title'))
        self.count_articles = browser.element((
            AppiumBy.ID, f'{self.locator_url}/item_reading_list_statistical_description'))

        self.list = browser.element((AppiumBy.ID, f'{self.locator_url}/recycler_view'))
        self.go_it_button = browser.element((AppiumBy.ID, f'{self.locator_url}/buttonView'))
        self.item_overflow_menu = browser.element((AppiumBy.ID, f'{self.locator_url}/item_overflow_menu'))

        self.button_edit_name_list = browser.element((AppiumBy.ID, f'{self.locator_url}/content'))
        self.text_input_name = browser.element((AppiumBy.ID, f'{self.locator_url}/text_input'))


    def click_tab_reading_lists(self):
        self.tab_reading_lists.click()

    def click_menu_overflow_button(self):
        self.menu_overflow_button.click()

    def click_overflow_create_new_list(self):
        self.overflow_create_new_list.click()

    def click_button_ok(self):
        self.button_ok.click()

    def title_should_be_visible(self):
        with step('Проверяем, что отображается наименование нового списка'):
            self.item_title_list.should(have.exact_text('My reading list'))

    def count_articles_should_be_visible(self):
        with step('Проверяем, что количество статей равно "0"'):
            self.count_articles.should(have.exact_text('0 articles'))

    def create_new_list(self):
        with step('Создаем новый список'):
            self.click_tab_reading_lists()
            self.click_menu_overflow_button()
            self.click_overflow_create_new_list()
            self.click_button_ok()

    def open_list(self):
        self.list.click()
        self.go_it_button.click()

    def edit_name_list(self):
        with step('Редактируем наименование списка'):
            self.open_list()
            self.item_overflow_menu.click()
            self.button_edit_name_list.click()
            self.text_input_name.type('Change name')
            self.click_button_ok()

    def title_should_be_change(self):
        with step('Проверяем, что наименование списка изменилось'):
            self.item_title_list.should(have.exact_text('Change name'))

