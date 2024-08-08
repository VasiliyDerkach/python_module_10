import pandas
import requests
import numpy
url = 'https://midural.ru/100034/100089/mu_leaders/'
resp = requests.get(url)
print(resp.content)
html1 = pandas.read_html(url)
print(html1)
alfa=numpy.array([55,0,15,4,3,15,3,1])
print(numpy.unique_counts(alfa))
#получаем массив из уникальных элементов заданного массива и для каждого уникального элемента количество таких элементов в заданном масииве