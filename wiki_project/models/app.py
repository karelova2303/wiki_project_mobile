from wiki_project.models.pages.reading_list_page import SavedPage
from wiki_project.models.pages.search_page import SearchPage
from wiki_project.models.pages.main_page import MainPage


class ApplicationManager:
    def __init__(self):
        self.search = SearchPage()
        self.main_page = MainPage()
        self.saved = SavedPage()

app = ApplicationManager()