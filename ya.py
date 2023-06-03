import time
import math

from selenium.webdriver.common.by import By
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

browser.implicitly_wait(5)

btn = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]').click()
tabs = browser.window_handles
#print(tabs)

browser.switch_to.window(tabs[1])

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
inputField = browser.find_element(By.ID, 'answer')
btnSubmit = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')

x_value = x_element.text
x = calc(int(x_value))

inputField.send_keys(x)
btnSubmit.click()

time.sleep(1)
