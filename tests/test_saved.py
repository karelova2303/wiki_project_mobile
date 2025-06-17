import allure
from allure_commons._allure import step

from wiki_project.models.app import app


@allure.tag('Mobile', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Сохраненные списки')
@allure.title('Создание нового списка')
def test_create_new_list():
    # WHEN
    with step('Пропускаем экран приветствия'):
        app.search.skip_start_screen()
    with step('Создаем новый список'):
        app.saved.create_new_list()

    # THEN
    with step('Проверяем отображение нового списка'):
        app.saved.should_be_visible_new_list()
        app.saved.should_be_visible_count_articles()


@allure.tag('Mobile', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Сохраненные списки')
@allure.title('Изменение списка')
def test_edit_list():
    # WHEN
    with step('Пропускаем экран приветствия'):
        app.search.skip_start_screen()
    with step('Создаем новый список'):
        app.saved.create_new_list()
    with step('Редактируем наименование списка'):
        app.saved.edit_name_list()

    # THEN
    with step('Проверяем, что изменения применились'):
        app.saved.should_be_change_name()
