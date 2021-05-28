import pytest
from selenium import webdriver
import time
import math

class TestPage():
    def test_should_see_button_add_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        assert browser.find_element_by_css_selector(".btn-add-to-basket")