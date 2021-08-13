from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AddMember:
    def __init__(self,driver:WebDriver):
        self._driver= driver
    def add_member(self):
        sleep(3)
        self._driver.find_element(By.ID,'username').send_keys('abcesdffff')
        self._driver.find_element(By.ID,'memberAdd_acctid').send_keys('abdbddsss')
        self._driver.find_element(By.Id,'memberAdd_phone').send_keys('12345612345')
        self._driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        sleep(5)

        return True
    def get_member(self):
        #elements = self._driver.find_element(By.CSS_SELECTOR,'')
        return  True