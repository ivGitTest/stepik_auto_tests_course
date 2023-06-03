from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

class TestRegForm(unittest.TestCase):
	def 	
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ��� ���, ������� ��������� ������������ ����
    #oblFields = browser.find_elements(By.CSS_SELECTOR, '.first_block input')

    fName = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    fName.send_keys('Ivan')

    lName = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    lName.send_keys('Petrov')

    email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    email.send_keys('xx@xx.ru')

    #for input in oblFields:
    #    input.send_keys('test value')

    time.sleep(2)

    # ���������� ����������� �����
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

    # ������� �������, ���������� �����
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    welcome_text = welcome_text_elt.text

    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(5)
    # ��������� ������� ����� ���� �����������
    browser.quit()