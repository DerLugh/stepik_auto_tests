from selenium import webdriver
import time
import unittest

class test_class_name(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_class_name("first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_class_name("first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("first_block .third")
        input3.send_keys("Test@test.ru")


        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "поломатушки")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_class_name("first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_class_name("first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("first_block .third")
        input3.send_keys("Test@test.ru")


        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "поломатушки")


if __name__ == "__main__":
    unittest.main()