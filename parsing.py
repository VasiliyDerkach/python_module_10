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
    #url = 'https://chkalovsky--svd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=case&case_id=436119774&case_uid=2854f329-d474-4336-8775-87b3fc142d77&delo_id=1540005'
    url = 'https://oktiabrsky--svd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=r&delo_id=1540005&case_type=0&new=0&G1_PARTS__NAMESS=&g1_case__CASE_NUMBERSS=&g1_case__JUDICIAL_UIDSS=&captcha=79609&captchaid=rl0l7t9813bfn0cjekdi7f5vj1&delo_table=g1_case&g1_case__ENTRY_DATE1D=&g1_case__ENTRY_DATE2D=&lawbookarticles%5B%5D=%D1%EF%EE%F0%FB%2C+%E2%EE%E7%ED%E8%EA%E0%FE%F9%E8%E5+%E8%E7+%F2%F0%F3%E4%EE%E2%FB%F5+%EE%F2%ED%EE%F8%E5%ED%E8%E9&G1_CASE__JUDGE=&g1_case__RESULT_DATE1D=&g1_case__RESULT_DATE2D=&G1_CASE__RESULT=&G1_CASE__BUILDING_ID=&G1_CASE__COURT_STRUCT=&G1_EVENT__EVENT_NAME=&G1_EVENT__EVENT_DATEDD=&G1_PARTS__PARTS_TYPE=&G1_PARTS__INN_STRSS=&G1_PARTS__KPP_STRSS=&G1_PARTS__OGRN_STRSS=&G1_PARTS__OGRNIP_STRSS=&G1_RKN_ACCESS_RESTRICTION__RKN_REASON=&g1_rkn_access_restriction__RKN_RESTRICT_URLSS=&g1_requirement__ACCESSION_DATE1D=&g1_requirement__ACCESSION_DATE2D=&G1_REQUIREMENT__CATEGORY=&g1_requirement__ESSENCESS=&g1_requirement__JOIN_END_DATE1D=&g1_requirement__JOIN_END_DATE2D=&G1_REQUIREMENT__PUBLICATION_ID=&G1_DOCUMENT__PUBL_DATE1D=&G1_DOCUMENT__PUBL_DATE2D=&G1_CASE__VALIDITY_DATE1D=&G1_CASE__VALIDITY_DATE2D=&G1_ORDER_INFO__ORDER_DATE1D=&G1_ORDER_INFO__ORDER_DATE2D=&G1_ORDER_INFO__ORDER_NUMSS=&G1_ORDER_INFO__EXTERNALKEYSS=&G1_ORDER_INFO__STATE_ID=&G1_ORDER_INFO__RECIP_ID=&Submit=%CD%E0%E9%F2%E8'
    driver.get(url)

    # elem = driver.find_element("q")
    # elem.send_keys("Hello WebDriver!")
    # elem.submit()
    # print(driver.current_window_handle)
    # print(driver.window_handles)
    # print(driver.title)
    # lst = driver.find_element(By.ID, 'cont2')
    # print(lst.text)
    #conts = {'tab1':('cont1','tablcont'),'tab2':('cont2','tablcont'),'tab3':('cont3','tablcont')}
    conts = {'None':('tablcont','tablcont')}
    recr = {}
    for cn, tx in conts.items():
        #lst = driver.find_element(By.ID,cn)
        if cn!='None': #если нет указания на кликабедьные элементы, которые надо предварительно активировать
            lst1 = driver.find_element(By.ID,cn)
            lst1.click()
        #time.sleep(5)
        #tc = driver.find_element(By.ID,tx[0])
        try:
            tc = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, tx[0]))
            )

            if tx[0]==tx[1]:
                htm = tc
            else:
                htm = tc.find_element(By.ID, tx[1])

            rows = htm.find_elements(by=By.TAG_NAME, value='tr')
            # подсчет количества столбцов
            tab = []
            for r in rows:
                cols = r.find_elements(by=By.TAG_NAME, value='td')
                cl = []

                # try:
                #     y = cols.get_attribute('href')
                #     if y:
                #         cl.append(y)
                # except:
                #     pass
                #refs = r.find_elements(by=By.TAG_NAME,value='ref')
                # for f in refs:
                #     print(f.text)
                for c in cols:
                    cl.append(c.text)
                    try:
                        y = c.find_element(by=By.TAG_NAME,value='a href=')
                        if y:
                            cl.append(y.text)
                    except:
                        pass
                if len(cl)>0:
                    tab.append(cl)
            # tabtxt = []
            # for r in tab:
            #     rowtxt = []
            #     for c in r:
            #         rowtxt.append(c.text)
                    #print(c.text,' | ',end='')
                #print('\n')
            if len(tab)>0:
                recr[cn] = tab
        except:
            print('не загрузилось')
    print(recr)
    print(len(recr))


    driver.quit()
"""    driver = Chrome()
    url = 'https://chkalovsky--svd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=r&delo_id=1540005&case_type=0&new=0&G1_PARTS__NAMESS=&g1_case__CASE_NUMBERSS=&g1_case__JUDICIAL_UIDSS=&captcha=65736&captchaid=16pihpfpksoa7ncagilpqli7e2&delo_table=g1_case&g1_case__ENTRY_DATE1D=&g1_case__ENTRY_DATE2D=&lawbookarticles%5B%5D=%D1%EF%EE%F0%FB%2C+%E2%EE%E7%ED%E8%EA%E0%FE%F9%E8%E5+%E8%E7+%F2%F0%F3%E4%EE%E2%FB%F5+%EE%F2%ED%EE%F8%E5%ED%E8%E9&G1_CASE__JUDGE=&g1_case__RESULT_DATE1D=&g1_case__RESULT_DATE2D=&G1_CASE__RESULT=&G1_CASE__BUILDING_ID=&G1_CASE__COURT_STRUCT=&G1_EVENT__EVENT_NAME=&G1_EVENT__EVENT_DATEDD=&G1_PARTS__PARTS_TYPE=&G1_PARTS__INN_STRSS=&G1_PARTS__KPP_STRSS=&G1_PARTS__OGRN_STRSS=&G1_PARTS__OGRNIP_STRSS=&G1_RKN_ACCESS_RESTRICTION__RKN_REASON=&g1_rkn_access_restriction__RKN_RESTRICT_URLSS=&g1_requirement__ACCESSION_DATE1D=&g1_requirement__ACCESSION_DATE2D=&G1_REQUIREMENT__CATEGORY=&g1_requirement__ESSENCESS=&g1_requirement__JOIN_END_DATE1D=&g1_requirement__JOIN_END_DATE2D=&G1_REQUIREMENT__PUBLICATION_ID=&G1_DOCUMENT__PUBL_DATE1D=&G1_DOCUMENT__PUBL_DATE2D=&G1_CASE__VALIDITY_DATE1D=&G1_CASE__VALIDITY_DATE2D=&G1_ORDER_INFO__ORDER_DATE1D=&G1_ORDER_INFO__ORDER_DATE2D=&G1_ORDER_INFO__ORDER_NUMSS=&G1_ORDER_INFO__EXTERNALKEYSS=&G1_ORDER_INFO__STATE_ID=&G1_ORDER_INFO__RECIP_ID=&Submit=%CD%E0%E9%F2%E8'
    driver.get(url)
    time.sleep(5)
    driver.quit()"""