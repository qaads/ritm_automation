import os
from dotenv import load_dotenv
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from loguru import logger
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

load_dotenv()

from site_pages.all_pages_list import AllPages as pages


logger.add("logs/site_test_{time:YYYY-MM-DD_HH:mm:ss}.log",
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
           level="DEBUG")

# logging the start and end of the test
@pytest.fixture(autouse=True, scope='function')
def log_test_progress(request):
    logger.info(f"run {request.node.name}:")
    yield
    logger.info(f"{request.node.name} is over")


# init context
@pytest.fixture(autouse=True ,scope='session')
def context():
    context = {}
    return context


@pytest.fixture
def get_webdriver(context, request):
    browser = request.param
    if browser == "chrome":
        logger.info(f"selenium_version: {selenium.__version__}")
        chrome_opt = webdriver.ChromeOptions()
        logger.debug(f"use_gui: {os.getenv('USE_GUI')}")
        if os.getenv('USE_GUI') == 0:
            chrome_opt.add_argument("--headless=new")
        else:
            chrome_opt.add_argument('start-maximized')
            chrome_opt.add_argument("window-size=1920x1080")
        chrome_opt.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_opt)
        logger.debug(f"browser_version: {driver.capabilities['browserVersion']}")
        logger.debug(f"driver inited: {driver}")
    if browser == "firefox": 
        logger.info(f"selenium_version: {selenium.__version__}")
        firefox_opt = webdriver.FirefoxOptions()
        logger.debug(f"use_gui: {os.getenv('USE_GUI')}")
        if os.getenv('USE_GUI') == 0:
            firefox_opt.add_argument("--headless")
        else: 
            firefox_opt.add_argument('--start-maximized')
            firefox_opt.add_argument('--window-size=1920,1080')
        firefox_opt.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_opt)
        logger.debug(f"browser_version: {driver.capabilities['browserVersion']}")
        logger.debug(f"driver inited: {driver}")
    context['driver'] = driver
    context['pages'] = pages()
    return driver


@pytest.fixture()
def setup_start_page(get_webdriver):
    driver = get_webdriver
    url = pages().start_page.url
    logger.debug(f"url: {url}")
    driver.get(url)
