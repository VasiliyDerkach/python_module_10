from threading import Thread
from queue import Queue, Empty
from time import sleep

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
    def busy(self, busy_status):
        self.is_busy = busy_status

class Cafe :
    def __init__(self, Tables):
        self.queue = Queue() # очередь прибывающих в кафе
        self.going = Queue() # очередь поевших в кафе на выход
        self.tables = Tables
        self.status = True #кафе закрыто/открыто работа до последнего посетителя
    def customer_arrival(self):
        for i in range(20):
            customer = Customer(i+1)
            self.queue.put(customer)
            print(f'Посетитель номер {customer.number} прибыл\n', end='')
            sleep(2)

    def busy(self, table_n, table_status):
        self.tables[table_n].busy(table_status)
    def serve_customer(self):

        customer = self.queue.get()
        while self.status:
            if customer.status in ('arrival','in queue'):
                for t in self.tables:
                    have_busy = False  # проверка наличия свободного стола
                    if not t.is_busy:
                        have_busy = True
                        t.busy(True)
                        customer.set_customer_status('table', t)
                        n = t.number
                        break
                if have_busy:
                    print(f'Посетитель номер {customer.number} сел за стол {n}.\n', end='')
                    #sleep(5)
                    self.going.put(customer)
                    try:
                        customer = self.queue.get()
                    except Empty:
                        print('Все пришедшие посетители сели за столы')
                        break
                else:
                    if customer.status!='in queue':
                        customer.set_customer_status('in queue', None)
                        print(f'Посетитель номер {customer.number} ожидает свободный стол.\n', end='')
            elif customer.status=='bouncer':
                break

    def go_customer(self):
        while True:
            try:
                custom = self.going.get(timeout=3)
            except Empty:
                print('Все пришедшие посетители поели и ушли')
                self.status = False
                # отправляем закрывающего кафе сотрудника
                customer = Customer(-1)
                customer.set_customer_status('bouncer',None)
                self.queue.put(customer)

                break
            if custom.status=='table':
                sleep(5)
                custom.table.busy(False)
                custom.set_customer_status('go', None)
                print(f'Посетитель номер {custom.number} покушал и ушёл\n', end='')

class Customer:
    def __init__(self, number):
        self.number = number
        self.status = 'arrival'
        self.table = None
    def set_customer_status(self,status,table):
        self.status = status
        self.table = table
    # Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_service = Thread(target=cafe.serve_customer)
customer_go = Thread(target=cafe.go_customer)

customer_arrival_thread.start()
customer_service.start()
customer_go.start()
# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
customer_service.join()
customer_go.join()
