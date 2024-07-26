
from datetime import datetime
from time import sleep
from threading import Thread
def wite_words(*args):

    newfile = open(args[1], mode='w' , encoding='utf-8')
    for i in range(1,args[0]+1):
        newfile.write(f'Какое-то слово № {i}\n')
        sleep(0.1)
    newfile.close()

time_start = datetime.now()
wite_words(10,  'example1.txt')

print('Завершилась запись в файл example1.txt')
wite_words(30,  'example2.txt')
print('Завершилась запись в файл example2.txt')
wite_words(200,  'example3.txt')
print('Завершилась запись в файл example3.txt')
wite_words(100,  'example4.txt')
print('Завершилась запись в файл example4.txt')

time_end = datetime.now()
print(time_end-time_start)
time_start = datetime.now()
thr_1 = Thread(target=wite_words,args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words,args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words,args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words,args=(100, 'example8.txt'))
thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()
thr_1.join()
print('Завершилась запись в файл example5.txt')
thr_2.join()
print('Завершилась запись в файл example6.txt')
thr_3.join()
print('Завершилась запись в файл example7.txt')
thr_4.join()
print('Завершилась запись в файл example8.txt')
time_end = datetime.now()
print(time_end-time_start)
