import allure

from wiki_project.data.data import test_text, text_python
from wiki_project.models.app import app

@allure.tag('Mobile', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Поиск по введенному тексту')
class TestSearch:

    @allure.title('Проверка результатов на совпадение текста')
    def test_search_by_text(self):
        # WHEN
        app.search.skip_start_screen()
        app.search.input_text_in_search(test_text)

        # THEN
        app.search.title_should_have_text(test_text)


    @allure.title('Проверка результатов на кликабельность')
    def test_click_the_item(self):
        # WHEN
        app.search.skip_start_screen()
        app.search.input_text_in_search(text_python)

        # THEN
        app.search.title_should_be_clickable()
