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
    url = 'https://asbestovsky--svd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=case&case_id=390794311&case_uid=a4534ef3-49d4-46c0-a04b-fc9e2ab5a9b4&delo_id=1540005'
    #url = 'https://oktiabrsky--svd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=r&delo_id=1540005&case_type=0&new=0&G1_PARTS__NAMESS=&g1_case__CASE_NUMBERSS=&g1_case__JUDICIAL_UIDSS=&captcha=36960&captchaid=lvl06vonmve1j68ilun3aeqph0&delo_table=g1_case&g1_case__ENTRY_DATE1D=&g1_case__ENTRY_DATE2D=&lawbookarticles%5B%5D=%D1%EF%EE%F0%FB%2C+%E2%EE%E7%ED%E8%EA%E0%FE%F9%E8%E5+%E8%E7+%F2%F0%F3%E4%EE%E2%FB%F5+%EE%F2%ED%EE%F8%E5%ED%E8%E9&G1_CASE__JUDGE=&g1_case__RESULT_DATE1D=&g1_case__RESULT_DATE2D=&G1_CASE__RESULT=&G1_CASE__BUILDING_ID=&G1_CASE__COURT_STRUCT=&G1_EVENT__EVENT_NAME=&G1_EVENT__EVENT_DATEDD=&G1_PARTS__PARTS_TYPE=&G1_PARTS__INN_STRSS=&G1_PARTS__KPP_STRSS=&G1_PARTS__OGRN_STRSS=&G1_PARTS__OGRNIP_STRSS=&G1_RKN_ACCESS_RESTRICTION__RKN_REASON=&g1_rkn_access_restriction__RKN_RESTRICT_URLSS=&g1_requirement__ACCESSION_DATE1D=&g1_requirement__ACCESSION_DATE2D=&G1_REQUIREMENT__CATEGORY=&g1_requirement__ESSENCESS=&g1_requirement__JOIN_END_DATE1D=&g1_requirement__JOIN_END_DATE2D=&G1_REQUIREMENT__PUBLICATION_ID=&G1_DOCUMENT__PUBL_DATE1D=&G1_DOCUMENT__PUBL_DATE2D=&G1_CASE__VALIDITY_DATE1D=&G1_CASE__VALIDITY_DATE2D=&G1_ORDER_INFO__ORDER_DATE1D=&G1_ORDER_INFO__ORDER_DATE2D=&G1_ORDER_INFO__ORDER_NUMSS=&G1_ORDER_INFO__EXTERNALKEYSS=&G1_ORDER_INFO__STATE_ID=&G1_ORDER_INFO__RECIP_ID=&Submit=%CD%E0%E9%F2%E8'
    driver.get(url)

    conts = {'tab1':('cont1','tablcont',[],'table'),'tab2':('cont2','tablcont',[],'table')
        ,'tab3':('cont3','tablcont',[],'table')
     ,'tab4':('cont4','tablcont',[],'table'), 'tab5':('cont5','cont_doc1',[],'doc')
        ,'tab6':('cont6','tablcont',[],'table'), 'tab7':('cont7','cont_doc1',[],'doc')}
    # 6  исп.листы? 7-кассац.опред.
    # conts  = {'tab5':('cont5','cont_doc1',[],'doc')}
    #conts = {'None':('tablcont','tablcont',[1],'table')}
    # ключ conts имя html закладки на сайте на которую надо переходить перед считыванием таблицы, если он None
    # значит страница сайта без закладок
    # первый элемент кортежа - имя html элемента, в который вложена таблица
    # второй элемент кортежа - имя html элемента таблицы (если совпадает с предыдущем, то таблицу сразу можно найти по ее имени)
    # третий элемент кортежа - список столбцов таблицы, которые надо проверить на наличие ссылок
    # если последний элемент пуст [] - то проверять на ссылки не надо. Ссылки добавляются в итоговую таблицу как доп.столбец справа
    recr = {}
    for cn, tx in conts.items():
        #lst = driver.find_element(By.ID,cn)
        flag_el =True
        if cn!='None': #если нет указания на кликабельные элементы, которые надо предварительно активировать
            #print(f'закладка {cn}')
            try:
                lst1 = driver.find_element(By.ID,cn)
                lst1.click()
            except:
                flag_el = False

        if flag_el:
            try:
                tc = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.ID, tx[0]))
                )
                # предусмотреть чтение заголовков таблиц
                if tx[0]==tx[1]:
                    htms[0] = tc
                else:
                    htms = tc.find_elements(By.ID, tx[1])
                    #предусмотреть случаи (реально есть), когда элементов tx[1] несколько на закладке (несколько таблиц)
                for htm in htms:
                    if tx[3]=='doc':
                        #print(htm.text)
                        thead = htm.text
                    elif tx[3]=='table':
                        try:
                            thead = htm.find_elements(by=By.TAG_NAME, value='th')
                        except:
                            thead = []
                        rows = htm.find_elements(by=By.TAG_NAME, value='tr')
                        # подсчет количества столбцов
                        tab = []
                        for r in rows:
                            cols = r.find_elements(by=By.TAG_NAME, value='td')
                            #refs = r.find_elements(by=By.TAG_NAME,value='ref')
                            # for f in refs:
                            #     print(f.text)
                            cl = []
                            ln = len(cols)
                            if isinstance(cols,list) and ln>0:
                                j = 0
                                for c in cols:
                                    cl.append(c.text)

                                    j += 1
                                    if len(tx[2])>0 and j in tx[2]:
                                        try:
                                            #rr = c.get_attribute('href')
                                            y = c.find_element(by=By.LINK_TEXT, value=c.text)
                                            if y:
                                                cl.append(y.get_attribute('href'))
                                        except Exception as ex0:
                                            pass
                            if len(cl)>0:
                                try:
                                    tab.append(cl)
                                except Exception as ecl:
                                    print(ecl)
                    thh = []
                    recr[cn]={}
                    if tx[3]=='table' and len(thead)>0:
                        for he in thead:
                            thh.append(he.text)
                        recr[cn]['head']=thh
                    elif tx[3]=='doc':
                        recr[cn]['head'] = thead
                    if len(tab)>0:
                        recr[cn]['table'] = tab
            except Exception as exc:
                print(f'не загрузилось {exc}')
    # for k,e in recr.items():
    #     print(('-------'))
    #     for p,ce in e['head']:
    #         print(ce)
    #      for p,ce in e['table']:
    #         print(ce)
    print(recr)

    driver.quit()
"""    driver = Chrome()
    url = 'https://chkalovsky--svd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=r&delo_id=1540005&case_type=0&new=0&G1_PARTS__NAMESS=&g1_case__CASE_NUMBERSS=&g1_case__JUDICIAL_UIDSS=&captcha=65736&captchaid=16pihpfpksoa7ncagilpqli7e2&delo_table=g1_case&g1_case__ENTRY_DATE1D=&g1_case__ENTRY_DATE2D=&lawbookarticles%5B%5D=%D1%EF%EE%F0%FB%2C+%E2%EE%E7%ED%E8%EA%E0%FE%F9%E8%E5+%E8%E7+%F2%F0%F3%E4%EE%E2%FB%F5+%EE%F2%ED%EE%F8%E5%ED%E8%E9&G1_CASE__JUDGE=&g1_case__RESULT_DATE1D=&g1_case__RESULT_DATE2D=&G1_CASE__RESULT=&G1_CASE__BUILDING_ID=&G1_CASE__COURT_STRUCT=&G1_EVENT__EVENT_NAME=&G1_EVENT__EVENT_DATEDD=&G1_PARTS__PARTS_TYPE=&G1_PARTS__INN_STRSS=&G1_PARTS__KPP_STRSS=&G1_PARTS__OGRN_STRSS=&G1_PARTS__OGRNIP_STRSS=&G1_RKN_ACCESS_RESTRICTION__RKN_REASON=&g1_rkn_access_restriction__RKN_RESTRICT_URLSS=&g1_requirement__ACCESSION_DATE1D=&g1_requirement__ACCESSION_DATE2D=&G1_REQUIREMENT__CATEGORY=&g1_requirement__ESSENCESS=&g1_requirement__JOIN_END_DATE1D=&g1_requirement__JOIN_END_DATE2D=&G1_REQUIREMENT__PUBLICATION_ID=&G1_DOCUMENT__PUBL_DATE1D=&G1_DOCUMENT__PUBL_DATE2D=&G1_CASE__VALIDITY_DATE1D=&G1_CASE__VALIDITY_DATE2D=&G1_ORDER_INFO__ORDER_DATE1D=&G1_ORDER_INFO__ORDER_DATE2D=&G1_ORDER_INFO__ORDER_NUMSS=&G1_ORDER_INFO__EXTERNALKEYSS=&G1_ORDER_INFO__STATE_ID=&G1_ORDER_INFO__RECIP_ID=&Submit=%CD%E0%E9%F2%E8'
    driver.get(url)
    time.sleep(5)
    driver.quit()"""

#решение суда /html/body/div[10]/div[3]/div/div[2]/div[2]/div[2]/div[5]/div[5]/div/div/span/p[1]
# <p style="TEXT-ALIGN: right; TEXT-INDENT: 0.5in">Мотивированное решение </p>
# cont_doc1 > span > p:nth-child(2)