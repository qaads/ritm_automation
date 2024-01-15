from pytest_bdd import when
from steps.methods_for_steps import *

    
@allure.step("Нажали на кнопку Element")
@when("Нажали на кнопку Element")
def clicked_on_element_button(context):
    logger.info(f"run step: clicked_on_element_button")
    clicked_on(context['driver'], context['pages'].start_page.elements_btn, "start_page._elements_btn")