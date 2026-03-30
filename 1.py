import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

class TestLoginUser():

    def test_guest_should_login_link(self, browser, load_config):
        print("start test")
        browser.get(link)
        button = browser.find_element(By.ID, "ember501")
        button.click()
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        login = browser.find_element(By.NAME, "login")
        login.send_keys(f"{login}")
        password = browser.find_element(By.NAME, "password")
        password.send_keys(f"{password}")
        enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        print("finish test")


