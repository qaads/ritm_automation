from site_pages.base_page import BasePage
import os
from dotenv import load_dotenv

load_dotenv

class StartPage(BasePage):
    url = os.getenv('URL')
    elements_btn = "//h5[text()='Elements']"
