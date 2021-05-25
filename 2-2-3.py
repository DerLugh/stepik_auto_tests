from selenium import webdriver
import time
import math

def calc(x_num, y_num):
  return str((int(x_num))+(int(y_num)))

link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()

try:
    browser.get(link)

    x_find = browser.find_element_by_id("num1")
    x_num = x_find.text
    print(x_num)
    y_find = browser.find_element_by_id("num2")
    y_num = y_find.text
    print(y_num)
    z = calc(x_num, y_num)
    print(z)
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла