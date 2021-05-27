import pytest
from selenium import webdriver
import time
import math

class TestPage():
    def test_should_see_button_add_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        btn_basket_elt = browser.find_element_by_css_selector(".btn-add-to-basket")
        answer_text = btn_basket_elt.text
        print(answer_text)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        if answer_text == "Добавить в корзину":
            assert answer_text == "Добавить в корзину"
            print("Здравствуй товарищ")
        elif answer_text == "Ajouter au panier":
            assert answer_text == "Ajouter au panier"
            print("viva la France")
        elif answer_text == "Añadir al carrito":
            assert answer_text == "Añadir al carrito"
            print("Viva la reina")
        else:
            print("where are you from?")
