from pytest_bdd import when
from steps.methods_for_steps import *
 

@allure.step("В раскрытом справа меню кликнули ЛКМ на Check Box")
@when("В раскрытом справа меню кликнули ЛКМ на Check Box")
def clicked_on_element_button(context):
    logger.info(f"run step: clicked_on_element_button")
    clicked_on(context['driver'], context['pages'].main_page.check_box_point, "main_page.check_box_point")