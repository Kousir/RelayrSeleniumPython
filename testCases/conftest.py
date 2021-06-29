from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

#Performing chrome driver configurations

@pytest.fixture()
def setup():
    opt = Options()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized')
    opt.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1})
    driver = webdriver.Chrome(r"C:\Users\kousir\Framework\Relayr\chromedriver.exe", options=opt)
    return driver

def pytest_addoption(parser):
   parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")