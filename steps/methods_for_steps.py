
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    NoSuchAttributeException,
    ElementNotInteractableException,
    ElementClickInterceptedException
)
import allure
from loguru import logger


def create_screenshot_for_allure(driver, screenshot_name: str):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=screenshot_name,
        attachment_type=allure.attachment_type.PNG
    )
    

# click on element
def clicked_on(driver, element_locator, element_name):
    logger.info(f"trying to find element ‘{element_name}’")
    try:
        driver.find_element(By.XPATH, element_locator)
        logger.info(f"element '{element_name}' found")
        logger.info(f"trying to click on element '{element_name}'")
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(EC.element_to_be_clickable((By.XPATH, element_locator))).click()
            logger.info(f"successfully clicked on element '{element_name}'")
        except (ElementClickInterceptedException, ElementNotInteractableException):
            try:
                driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, element_locator))
                logger.info(f"successfully clicked on element '{element_name}'")
            except Exception as e:
                logger.error(f"failed to click on element '{element_name}'")
                create_screenshot_for_allure(driver, f"failed to click on element '{element_name}'")
                raise e(f"failed to click on element '{element_name}'")
    except NoSuchElementException:
        logger.error(f"element '{element_name}' could not be found")
        create_screenshot_for_allure(driver, f"element '{element_name}' could not be found")
        raise NoSuchElementException(f"element '{element_name}' could not be found")
    
# check availability element (with text)
def checking_an_element_with_text(driver, ref_text, element_locator, element_name):
    reference_text = ref_text
    logger.info(f"trying to find element ‘{element_name}’")
    try:
        el = driver.find_element(By.XPATH, element_locator)
        logger.info(f"element '{element_name}' found")
        try:
            logger.info(f"attempt to get text from element '{element_name}'")
            text = el.get_attribute('textContent')
            logger.info(f"got the text from the element '{element_name}': {text}")
        except NoSuchAttributeException:
            logger.error(f"element '{element_name}' does not contain text")
            raise NoSuchAttributeException(f"element '{element_name}' does not contain text")
    except NoSuchElementException:
        logger.error(f"element '{element_name}' could not be found")
        create_screenshot_for_allure(driver, f"element '{element_name}' could not be found")
        raise NoSuchElementException(f"element '{element_name}' could not be found")
    logger.info(f"compare the found text from '{element_name}' with the reference one")
    logger.debug(f"found text = {text}")
    logger.debug(f"reference text = {reference_text}")
    try:
        assert text == reference_text
        logger.info(f"texts match")
    except AssertionError:
        logger.error(f"text from element '{element_name}’ is incorrect")
        create_screenshot_for_allure(driver, f"text from element '{element_name}’ is incorrect")
        raise AssertionError(f"text from element '{element_name}' is incorrect")
    

# Открыта страница 
def checking_that_page_is_open(driver, ref_url, context):
    logger.info(f"compare current url with reference url")
    current_url = driver.current_url
    reference_url = ref_url
    logger.debug(f"current url = {current_url}")
    logger.debug(f"reference url = {reference_url}")
    try:
        assert current_url == reference_url
        logger.info(f"urls match")
    except AssertionError:
        logger.error(f"urls don't match")
        create_screenshot_for_allure(driver, f"urls don't match")
        raise AssertionError("urls don't match")
