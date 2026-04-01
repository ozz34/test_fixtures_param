import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nfinish browser for test..")
    browser.quit()

@pytest.fixture(scope="function")
def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config
