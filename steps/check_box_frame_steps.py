from pytest_bdd import when, then
from steps.methods_for_steps import *


@allure.step("Расскрыли директорию Home")
@when("Расскрыли директорию Home")
def opened_home_dir(context):
    logger.info(f"run step: opened_home_dir")
    clicked_on(context['driver'], context['pages'].check_box_frame.home_divider,
               "check_box_frame.home_divider")
    

@allure.step("Расскрыли директорию Downloads")
@when("Расскрыли директорию Downloads")
def opened_downloads_dir(context):
    logger.info(f"run step: opened_downloads_dir")
    clicked_on(context['driver'], context['pages'].check_box_frame.downloads_divider,
               "check_box_frame.downloads_divider")
  
  
@allure.step("Выбрали чекбос Word File.doc")
@when("Выбрали чекбос Word File.doc")
def selected_word_file_check_box(context):
    logger.info(f"run step: selected_word_file_check_box")
    clicked_on(context['driver'], context['pages'].check_box_frame.word_file_check_box,
               "check_box_frame.word_file_check_box")    


@allure.step("Появилось сообщение 'You have selected: wordFile'")
@then("Появилось сообщение 'You have selected: wordFile'")
def message_you_have_selected_wordfile_appeared(context):
    logger.info(f"run step: message_you_have_selected_wordfile_appeared")
    checking_an_element_with_text(context['driver'], "You have selected :wordFile", 
                                  context['pages'].check_box_frame.result_str, "check_box_frame.result_str")
