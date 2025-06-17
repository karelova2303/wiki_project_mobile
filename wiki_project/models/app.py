from wiki_project.models.pages.saved_page import SavedPage
from wiki_project.models.pages.search_page import SearchPage
from wiki_project.models.pages.start_screen_page import StartScreenPage


class ApplicationManager:
    def __init__(self):
        self.search = SearchPage()
        self.start_screen = StartScreenPage()
        self.saved = SavedPage()

app = ApplicationManager()