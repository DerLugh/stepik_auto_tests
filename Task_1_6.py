from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()

try:
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys("d")
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("d")
    input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    input3.send_keys("d")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла