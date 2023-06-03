import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestYandex(unittest.TestCase):
    def test_searchField(self):
        browser = webdriver.Chrome()
        browser.get('http://ya.ru')
        searchField = browser.find_element(By.ID, 'js-button')
        self.assertEqual(searchField.get_attribute('type'), 'submit', 'Атрибут "type" != "submit"')

if __name__ == "__main__":
    unittest.main()


