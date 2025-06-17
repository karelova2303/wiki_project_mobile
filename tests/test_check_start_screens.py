import allure
from allure_commons._allure import step

from wiki_project.data.data import text_screen_one, text_screen_two, text_screen_three, text_screen_four
from wiki_project.models.app import app


@allure.tag('Mobile', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Экраны приветствия')
@allure.title('Проверка отображения экранов приветствия')
def test_check_start_screens():
    with step('Проверка первого экрана приветствия'):
        app.start_screen.should_have_text_on_the_screen(text_screen_one)

    with step('Кликнуть кнопку "Continue"'):
        app.start_screen.click_forward_button()

    with step('Проверка второго экрана приветствия'):
        app.start_screen.should_have_text_on_the_screen(text_screen_two)

    with step('Кликнуть кнопку "Continue"'):
        app.start_screen.click_forward_button()

    with step('Проверка третьего экрана приветствия'):
        app.start_screen.should_have_text_on_the_screen(text_screen_three)

    with step('Кликнуть кнопку "Continue"'):
        app.start_screen.click_forward_button()

    with step('Проверка четвертого экрана приветствия'):
        app.start_screen.should_have_text_on_the_screen(text_screen_four)

    with step('Кликнуть кнопку "Get started"'):
        app.start_screen.click_done_button()

    with step('Проверка главной страницы'):
        app.start_screen.should_be_visible_main_page()
