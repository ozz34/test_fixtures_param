import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

class TestLoginUserAndCorrectAnswer():
    
    @pytest.mark.parametrize('link', [
                                      "https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"
                                    ]
                              )
    def test_login_and_correct_answer(self, browser, load_config, link):
        print("start test login")
        browser.get(link)
        button = browser.find_element(By.ID, "ember501")
        button.click()
        login = browser.find_element(By.NAME, "login")
        required_login = load_config['login_stepik']
        login.send_keys(f"{required_login}")
        password = browser.find_element(By.NAME, "password")
        required_password = load_config['password_stepik']
        password.send_keys(f"{required_password}")
        enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        enter.click()
        print("finish test login")
        print("start test correct answer")
        textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        textarea.clear()
        assert textarea.get_property("value") == "", "Поле не очистилось!"
        answer = math.log(int(time.time()))
        textarea.send_keys(f"{answer}")
        send_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        send_button.click()
        time.sleep(5)
        result_text = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        ).text
        assert result_text == "Correct!", f"Должно быть сообщение Correct!, но в выводе сообщение {result_text}"
        print("finish test correct answer")





