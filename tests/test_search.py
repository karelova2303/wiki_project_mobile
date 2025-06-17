import allure
from allure_commons._allure import step

from wiki_project.data.data import test_text, text_python
from wiki_project.models.app import app


@allure.tag('Mobile', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Поиск по введенному тексту')
@allure.title('Проверка результатов на совпадение текста')
def test_search_by_text():
    # WHEN
    with step('Пропускаем экран приветствия'):
        app.search.skip_start_screen()
    with step('Вводим текст в строку поиска'):
        app.search.input_text_in_search(test_text)

    # THEN
    with step('Проверяем найденный контент'):
        app.search.should_have_text_title(test_text)


@allure.tag('Mobile', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Поиск по введенному тексту')
@allure.title('Проверка результатов на кликабельность')
def test_click_the_item():
    # WHEN
    with step('Пропускаем экран приветствия'):
        app.search.skip_start_screen()
    with step('Вводим текст в строку поиска'):
        app.search.input_text_in_search(text_python)

    # THEN
    with step('Проверяем, что найденный контент кликабельный'):
        app.search.should_be_clickable_title()
