from pytest_bdd import given
from steps.methods_for_steps import *


@allure.step("Открыта стартовая страница сайта")
@given("Открыта стартовая страница сайта")
def check_that_site_start_page_is_opened(context):
    logger.info(f"run step: check_that_site_start_page_is_opened")
    checking_that_page_is_open(context['driver'], context['pages'].start_page.url, context)