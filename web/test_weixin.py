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
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()


    def test_weixin(self):
        # 获取cookies
        web_cookies = self.driver.get_cookies()
        print('-----',web_cookies)

        # 将cookies存储起来
        # db = shelve.open('web_cookies')
        # cookies = [{'domain': '.ceshiren.com', 'httpOnly': False, 'name': 'Hm_lpvt_214f62eef822bde113f63fedcab70931', 'path': '/', 'secure': False, 'value': '1603603782'}, {'domain': 'ceshiren.com', 'expiry': 1608789798, 'httpOnly': True, 'name': '_t', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '7c1fa472a8d2b110187414aaed2f2cae'}, {'domain': 'ceshiren.com', 'httpOnly': True, 'name': '_forum_session', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'VzRsZnBaOXhjUXZWRXRvZ3RKcXF1M05wZUE1R2Q5RHB2c0RMUlgxV1FJOG8vZFRjU3pOanQ4RUk3Wk5PVDYrRjBVeU5DUFV5R2tOMEF4M1BrZUNUWEcwYjl6N1krSG51RC9HRHhLL01kRXhHelBlbnIrditNRnNITm81cUYvakM3bWpYMDZEKy9xanNUZWFvdW1lY1VzMWtEaVhIak1EZWpIeVF1ZlEyL3hzaW5SZjFaeXhEbk5KMHNac1UwUTFaLS1zRndhZkVINU5zQ3h1ZDhjWE52UUt3PT0%3D--e67c23276cc38feb2e8167ff96f0f8f3e0e7b6c8'}, {'domain': '.ceshiren.com', 'expiry': 1635139782, 'httpOnly': False, 'name': 'Hm_lvt_214f62eef822bde113f63fedcab70931', 'path': '/', 'secure': False, 'value': '1603203339,1603287086,1603598832,1603603782'}, {'domain': '.ceshiren.com', 'expiry': 1603690182, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.822765733.1603598832'}, {'domain': '.ceshiren.com', 'expiry': 1666675782, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.97234589.1600577654'}]
        # db['web_cookies'] = cookies
        # print('++++', type(db['web_cookies']))
        # db.close()

        # 获取cookies
        db = shelve.open('web_cookies')
        web_cookies1 = db['web_cookies']
        db.close()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        for cookie in web_cookies1:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys('D:\\partner.xlsx')
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "partner.xlsx" == filename
