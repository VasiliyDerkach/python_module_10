import pandas
import requests
import numpy
url = 'https://midural.ru/100034/100089/mu_leaders/'
resp = requests.get(url)
print(resp.content)
print(resp.headers)
html1 = pandas.read_html(url)
print(html1)
excl = pandas.DataFrame({'Cat': ['Pers','Scotish','BRIT']
                         ,'LENGTH': [250,200,300]
                         ,'Color':['White','Grey','Many']})

excl.to_excel('cats.xlsx')
alfa=numpy.array([55,0,15,4,3,15,3,1])
un, count_un =numpy.unique_counts(alfa)
#получаем массив из уникальных элементов заданного массива и для каждого уникального элемента количество таких элементов в заданном масиивеdt = numpy.dot(un,count_un) #скалярное произведение двух массивов
print(un , count_un)
dt = numpy.dot(un, count_un) #скалярное произвдение двух массивов
print(dt)
