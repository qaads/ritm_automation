from pytest_bdd import scenario
import pytest
import allure
from steps.common_steps import *
from steps.check_box_frame_steps import *
from steps.main_page_steps import *
from steps.start_page_steps import *
from steps.methods_for_steps import *


ALLURE_FEATURE = "Проверка сайта DEMOQA"
ALLURE_STORY = "Проверка Check Box"

@pytest.mark.parametrize("get_webdriver", ["firefox", "chrome"], indirect=True)
@allure.feature(ALLURE_FEATURE)
@allure.story(ALLURE_STORY)
@allure.title("Проверка чек-бокса Word File")
@scenario('../scenarios/check_box.feature',
          "Проверка чек-бокса Word File")
def test_1(
    get_webdriver,
    setup_start_page
):
    pass
