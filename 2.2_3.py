import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

filename = 'test.txt'
currentFolder = os.path.abspath(os.path.dirname(__file__))
filPath = os.path.join(currentFolder, filename)

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
time.sleep(1)

browser

fName = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
fName.send_keys('Ivan')

lName = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
lName.send_keys('Petrov')

email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"')
email.send_keys('xx@xx.ru')

fileLoad = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
fileLoad.send_keys(filPath)
#time.sleep(1)

btn = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()
time.sleep(4)
'''
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
textField = browser.find_element(By.CSS_SELECTOR, '#answer')

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
'''
browser.quit()


