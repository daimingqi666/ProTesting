from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AddMember:
    def __init__(self,driver:WebDriver):
        self._driver= driver
    def add_member(self):

        self._driver.find_element(By.ID,'username').send_keys('abcesdffff')
        self._driver.find_element(By.ID,'memberAdd_acctid').send_keys('abdbddsss')

        self._driver.find_element(By.NAME,'mobile').send_keys('12345612345')
        self._driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        sleep(5)

        return True
    def get_member(self):
        sleep(2)
        table = self._driver.find_element(By.ID,'member_list')
        sleep(2)
        return[element.get_attribute("title") for element in table.find_elements_by_name("td")]
        #sleep(3)
        #return  True

    '''
    table 
      tr
        <td title=" >
        td 6
        
     tr
     trable
    '''