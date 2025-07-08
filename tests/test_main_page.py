import allure

from wiki_project.data.data import text_screen_one, text_screen_two, text_screen_three, text_screen_four
from wiki_project.models.app import app

@allure.tag('Mobile', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Главная страница')
class TestMainPage:

    @allure.title('Проверка загрузки главной страницы')
    def test_check_start_screens(self):
        # WHEN
        app.main_page.should_have_text_on_the_screen(text_screen_one)
        app.main_page.click_forward_button()
        app.main_page.should_have_text_on_the_screen(text_screen_two)
        app.main_page.click_forward_button()
        app.main_page.should_have_text_on_the_screen(text_screen_three)
        app.main_page.click_forward_button()
        app.main_page.should_have_text_on_the_screen(text_screen_four)
        app.main_page.click_done_button()

        # THEN
        app.main_page.main_page_appears()
