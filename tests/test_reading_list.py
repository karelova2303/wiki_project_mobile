import allure

from wiki_project.models.app import app


@allure.tag('Mobile', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Сохраненные списки')
class TestReadingList:

    @allure.title('Создание нового списка')
    def test_create_new_list(self):
        # WHEN
        app.search.skip_start_screen()
        app.saved.create_new_list()

        # THEN
        app.saved.title_should_be_visible()
        app.saved.count_articles_should_be_visible()


    @allure.title('Изменение названия списка')
    def test_edit_list(self):
        # WHEN
        app.search.skip_start_screen()
        app.saved.create_new_list()
        app.saved.edit_name_list()

        # THEN
        app.saved.title_should_be_change()
