from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
if __name__ == '__main__':
    #option = Options()
    #option.add_argument("--disable-infobars")
    driver = Chrome()
    #driver = Chrome(executable_path='C:/distrib/chromedriver.exe',options=option)
    url = 'https://verhisetsky--svd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=case&case_id=444088738&case_uid=ce547281-8ebc-485f-b239-ed95d04dfd0a&delo_id=1540005'
    driver.get(url)

    # elem = driver.find_element("q")
    # elem.send_keys("Hello WebDriver!")
    # elem.submit()
    # print(driver.current_window_handle)
    # print(driver.window_handles)
    # print(driver.title)
    # lst = driver.find_element(By.ID, 'cont2')
    # print(lst.text)
    conts = {'tab1':'cont1','tab2':'cont2','tab3':'cont3'}
    for cn, tx in conts.items():
        #lst = driver.find_element(By.ID,cn)
        lst1 = driver.find_element(By.ID,cn)
        lst1.click()
        tc = driver.find_element(By.ID,tx)
        print(lst1.text)
        print(tc.text)
