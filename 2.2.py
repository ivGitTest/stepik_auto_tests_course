import math
import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
time.sleep(2)

def calc(x, y):
#    return str(math.log(abs(12 * math.sin(int(x)))))
    return x + y

#trs = browser.find_element(By.CSS_SELECTOR, '#treasure')

#x_element = trs.get_attribute('valuex') # browser.find_element(By.CSS_SELECTOR, '#input_value')
num1_text = browser.find_element(By.CSS_SELECTOR,'#num1')
num2_text = browser.find_element(By.CSS_SELECTOR, '#num2')

select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))

#textField = browser.find_element(By.CSS_SELECTOR, '#answer')
#chBox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
#rBtn = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
btn = browser.find_element(By.CSS_SELECTOR, '.btn-default')

x, y = int(num1_text.text), int(num2_text.text)
y = calc(x, y)

select.select_by_visible_text(str(y))
time.sleep(1)
#textField.send_keys(y)

#chBox.click()
#rBtn.click()
btn.click()

time.sleep(5)

browser.quit()


