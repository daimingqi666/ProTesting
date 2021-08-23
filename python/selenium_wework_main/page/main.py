from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from python.selenium_wework_main.page.add_member import AddMember


class Main:
    def __init__(self):

        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self._driver = webdriver.Chrome(options=options)

        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
    def goto_add_member(self):
        #click add_member
        #self._driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)')
        #self._driver.find_element(By.ID,'menu_contacts').click()
        #self._driver.find_element(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        self._driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        sleep(5)
        return AddMember(self._driver)