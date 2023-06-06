import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser

class TestVisibleComponents():
#    @classmethod
#    def setup_class(self):
#        self.browser = webdriver.Chrome()
#        self.browser.implicitly_wait(5)
#        self.host = 'https://dev2-mm.srvdev.ru'
#        self.api = '/portal'

#    @classmethod
#    def teardown_class(self):
#        self.browser.quit()

    def test_siteIsAccess(self, browser):
        host = 'https://dev2-mm.srvdev.ru'
        api = '/portal'
        browser = webdriver.Chrome()
        partOfURL = 'https://dev2-mm.srvdev.ru/portal' #.auth/signin'
        browser.implicitly_wait(5)

        browser.get(host + api)
        assert partOfURL in browser.current_url

        browser.quit()

    def test_findLogos(self, browser):
        host = 'https://dev2-mm.srvdev.ru'
        api = '/portal'
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        browser.get(host + api)
        logo1 = browser.find_element(By.CSS_SELECTOR, '.login-logo > .logo-icon')
        logo2 = browser.find_element(By.CSS_SELECTOR, '.login-logo > .logo-text')
        assert logo1.get_attribute('src') == host + api + ".auth/assets/mosmetro_vert_sign.svg"
        assert logo2.get_attribute('src') == host + api + ".auth/assets/mosmetro_vert_text.svg"

        browser.quit()
'''
    username = browser.find_element(By.XPATH, '//input[@name="username"]')# "div.mat-form-field-infix > #username")
    password = browser.find_element(By.XPATH, '//input[@name="password"]') #".mat-form-field-infix #current-password")
    enterButton = browser.find_element(By.XPATH, '//button/span[text()="Войти"]')# ".mat-button-base")

    username.send_keys("irybakov")
    password.send_keys("Test1234")

    enterButton.click()
    time.sleep(2)

    time.sleep(5)

def goToContractManagement():
    link = browser.find_element(By.CSS_SELECTOR,'a[href = "/portal/areas/pcr/contractors"]')
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});",link)
    #time.sleep(1)
    link.click()
    time.sleep(1)

def goToAddExtContractor():
    link = browser.find_element(By.CSS_SELECTOR, 'button[routerlink = "/areas/pcr/add-ext-contractor"]')
    link.click()
    time.sleep(1)

def createContractor():
    fullName = browser.find_element(By.XPATH, '//mat-label[text()="Полное наименование"]/ancestor::div[contains(@class,"mat-form-field-infix")]/input') #Полное наименование
    shortName = browser.find_element(By.XPATH, '//mat-label[text()="Краткое наименование"]/ancestor::div[contains(@class,"mat-form-field-infix")]/input') #Краткое наименование
#    code = browser.find_element(By.ID, '#mat-input-2') #Код
#    fullName2 = browser.find_element(By.ID, '#mat-input-5')  #Полное наименование
#    shortName2 = browser.find_element(By.ID, '#mat-input-6') #Сокращенное наименование
#    TypeCompany = browser.find_element(By.ID, '#mat-select-2').click()  #Тип ЮЛ
#    TypeCompanyOption = browser.find_element(By.XPATH, '//mat-option[@id = "mat-option-3"]/span[@class = "mat-option-text"][text() = "Акционерное общество"]')
#    INN = browser.find_element(By.ID, '#mat-input-8') #ИНН
#    KPP = browser.find_element(By.ID, '#mat-input-9')  #КПП
#    OGRN = browser.find_element(By.ID, '#mat-input-8') #ОГРН
#    OKPO = browser.find_element(By.ID, '#mat-input-9')  #ОКПО

    fullName.send_keys('ЮЛ1')
    shortName.send_keys('ЮЛ1')
#   #code.send_keys('ЮЛ1')
#   fullName2.send_keys('ЮЛ1')
#    shortName2.send_keys('ЮЛ1')
#    TypeCompanyOption.click()
#    INN.send_keys('111111111111')
#    KPP.send_keys('222222222')
#    OGRN.send_keys('3333333333333')
#    OKPO.send_keys('4444444444')


login()
createContractor()
time.sleep(10)
#goToContractManagement()
#goToAddExtContractor()
'''
#browser.quit()
