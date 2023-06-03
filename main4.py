import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(3)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

#price = browser.find_element(By.XPATH, '//h5[@id = "price"].text()')
button = browser.find_element(By.ID, 'book')
button2 = browser.find_element(By.ID, 'solve')
input = browser.find_element(By.ID, 'answer')

price100 = WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.XPATH, '//h5[@id = "price"]'), '$100'))

button.click()
time.sleep(1)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
x = int(x_element)
input.send_keys(calc(x))
button2.click()
time.sleep(5)

browser.quit()