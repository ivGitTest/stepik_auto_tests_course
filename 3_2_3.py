from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegOnSite(unittest.TestCase):
	def test_one(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		# Ваш код, который заполняет обязательные поля
		#oblFields = browser.find_elements(By.CSS_SELECTOR, '.first_block input')

		fName = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
		fName.send_keys('Ivan')

		lName = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
		lName.send_keys('Petrov')

		email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
		email.send_keys('xx@xx.ru')

		time.sleep(1)

		# Отправляем заполненную форму
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Что то пошло не так')

	def test_two(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		# Ваш код, который заполняет обязательные поля
		#oblFields = browser.find_elements(By.CSS_SELECTOR, '.first_block input')

		fName = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
		fName.send_keys('Ivan')

		lName = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
		lName.send_keys('Petrov')

		email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
		email.send_keys('xx@xx.ru')

		time.sleep(1)

		# Отправляем заполненную форму
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Что то пошло не так')


if __name__ == "__main__":
	unittest.main()