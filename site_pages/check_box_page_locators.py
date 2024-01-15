from site_pages.main_page_locators import MainPage

class CheckBoxFrame(MainPage):
    home_divider = "//span[text()='Home']/../../button"
    downloads_divider = "//span[text()='Downloads']/../../button"
    word_file_check_box = "//span[contains(text(), 'Word File')]"
    result_str = "//div[@id='result']"
    