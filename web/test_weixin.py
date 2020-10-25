import shelve

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeixin():

    def setup_method(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self):
        self.driver.quit()


    def test_weixin(self):
        # 获取cookies
        web_cookies = self.driver.get_cookies()

        # 将cookies存储起来
        # db = shelve.open('web_cookies')
        # db['web_cookies'] = web_cookies
        # db.close()

        # 获取cookies
        db = shelve.open('web_cookies')
        web_cookies1 = db['web_cookies']
        db.close()
        for cookie in web_cookies1:
            self.driver.add_cookie()
        self.driver.refresh()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.ID,'menu_contacts').click()
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys('D:\\partner.xlsx')
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "partner.xlsx" == filename
