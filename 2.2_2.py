import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')
time.sleep(2)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
textField = browser.find_element(By.CSS_SELECTOR, '#answer')
btn = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
chBox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
rBtn = browser.find_element(By.CSS_SELECTOR, '#robotsRule')

x = int(x_element.text)
y = calc(x)

textField.send_keys(y)
#time.sleep(1)

chBox.click()

browser.execute_script('return arguments[0].scrollIntoView(true);', rBtn)
#time.sleep(1)

rBtn.click()
#time.sleep(1)

browser.execute_script('return arguments[0].scrollIntoView(true);', btn)
#time.sleep(1)

btn.click()
time.sleep(5)

browser.quit()


