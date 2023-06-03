import math
import time

from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/math.html')
time.sleep(2)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
textField = browser.find_element(By.CSS_SELECTOR, '#answer')
chBox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
rBtn = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
btn = browser.find_element(By.CSS_SELECTOR, '.btn-default')

x = x_element.text
y = calc(x)

textField.send_keys(y)

chBox.click()
rBtn.click()
btn.click()

time.sleep(2)

browser.quit()


