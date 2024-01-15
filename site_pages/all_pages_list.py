from site_pages.base_page import BasePage
from site_pages.start_page_locators import StartPage
from site_pages.check_box_page_locators import CheckBoxFrame
from site_pages.main_page_locators import MainPage

class AllPages():
    def __init__(self):
        self.base_page = BasePage()
        self.start_page = StartPage()
        self.main_page = MainPage()
        self.check_box_frame = CheckBoxFrame()