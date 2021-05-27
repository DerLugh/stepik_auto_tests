import pytest
from selenium import webdriver
import time
import math

class TestMainPage():
    @pytest.mark.parametrize('link_test', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_guest_should_see_login_link(self, browser, link_test, answer_all_test):
        link = f"https://stepik.org/lesson/{link_test}/step/1"
        browser.get(link)
        time.sleep(3)

        answer = math.log(int(time.time()))
        print(answer)
        input_answer = browser.find_element_by_tag_name("textarea")
        input_answer.send_keys(str(answer))

        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()

        time.sleep(1)

        find_text_elt = browser.find_element_by_class_name("ember-view pre")
        answer_text = find_text_elt.text
        print(answer_text)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        if answer_text != "Correct!":
            answer_all_test += answer_all_test
            print(answer_all_test)
        assert answer_text == "Correct!"
