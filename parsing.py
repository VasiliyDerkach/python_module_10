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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    conts = {'tab1':('cont1','ДЕЛО'),'tab2':('cont2','ДВИЖЕНИЕ ДЕЛА'),'tab3':('cont3','СТОРОНЫ ПО ДЕЛУ')}
    for cn, tx in conts.items():
        #lst = driver.find_element(By.ID,cn)
        lst1 = driver.find_element(By.ID,cn)
        lst1.click()
        #tc = driver.find_element(By.ID,tx[0])
        try:
            tc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, tx[0]))
            )
            print(tc.text)
            htm = tc.find_element(By.ID, "tablcont")
            #print(htm.text)
            rows = htm.find_elements(by=By.TAG_NAME, value='tr')
            # подсчет количества столбцов
            cols = htm.find_elements(by=By.TAG_NAME, value='td')
            print(len(rows),len(cols))

            #htm = tc.find_element(By.ID,'tablcont')
            #htm = driver.page_source
            #htm1 = pd.read_html(htm, match=tx[1])
            #print(htm.text)
        except:
            print('не загрузилось')

        #time.sleep(5)
        # while not tc.is_displayed():
        #     pass

        # #print(lst1.text)

        # with open('delo.txt',mode='w',encoding='utf-8') as f:
        #     f.write(tc.text)

    driver.quit()
"""    driver = Chrome()
    url = 'https://chkalovsky--svd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=r&delo_id=1540005&case_type=0&new=0&G1_PARTS__NAMESS=&g1_case__CASE_NUMBERSS=&g1_case__JUDICIAL_UIDSS=&captcha=65736&captchaid=16pihpfpksoa7ncagilpqli7e2&delo_table=g1_case&g1_case__ENTRY_DATE1D=&g1_case__ENTRY_DATE2D=&lawbookarticles%5B%5D=%D1%EF%EE%F0%FB%2C+%E2%EE%E7%ED%E8%EA%E0%FE%F9%E8%E5+%E8%E7+%F2%F0%F3%E4%EE%E2%FB%F5+%EE%F2%ED%EE%F8%E5%ED%E8%E9&G1_CASE__JUDGE=&g1_case__RESULT_DATE1D=&g1_case__RESULT_DATE2D=&G1_CASE__RESULT=&G1_CASE__BUILDING_ID=&G1_CASE__COURT_STRUCT=&G1_EVENT__EVENT_NAME=&G1_EVENT__EVENT_DATEDD=&G1_PARTS__PARTS_TYPE=&G1_PARTS__INN_STRSS=&G1_PARTS__KPP_STRSS=&G1_PARTS__OGRN_STRSS=&G1_PARTS__OGRNIP_STRSS=&G1_RKN_ACCESS_RESTRICTION__RKN_REASON=&g1_rkn_access_restriction__RKN_RESTRICT_URLSS=&g1_requirement__ACCESSION_DATE1D=&g1_requirement__ACCESSION_DATE2D=&G1_REQUIREMENT__CATEGORY=&g1_requirement__ESSENCESS=&g1_requirement__JOIN_END_DATE1D=&g1_requirement__JOIN_END_DATE2D=&G1_REQUIREMENT__PUBLICATION_ID=&G1_DOCUMENT__PUBL_DATE1D=&G1_DOCUMENT__PUBL_DATE2D=&G1_CASE__VALIDITY_DATE1D=&G1_CASE__VALIDITY_DATE2D=&G1_ORDER_INFO__ORDER_DATE1D=&G1_ORDER_INFO__ORDER_DATE2D=&G1_ORDER_INFO__ORDER_NUMSS=&G1_ORDER_INFO__EXTERNALKEYSS=&G1_ORDER_INFO__STATE_ID=&G1_ORDER_INFO__RECIP_ID=&Submit=%CD%E0%E9%F2%E8'
    driver.get(url)
    time.sleep(5)
    driver.quit()"""