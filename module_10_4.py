from threading import Thread
from queue import Queue
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
        self.waiting = Queue() # очередь ожидающих столика в кафе
        self.to_out = Queue() # очередь для завершения обсуживания
        self.tables = Tables
    def customer_arrival(self):
        for i in range(20):
            customer = Customer(i+1)
            self.queue.put(customer)
            print(f'Посетитель номер {customer.number} прибыл')
            sleep(1)

    def busy(self, table_n, table_status):
        self.tables[table_n].busy(table_status)
    def serve_customer(self):
        if self.waiting.qsize()>0:
            customer = self.waiting.get()
        else:
            customer = self.queue.get()
        while customer:
            if customer.status in ('arrival','in queue'):
                have_busy = False #проверка наличия свободного стола

                for t in self.tables:

                    if not t.is_busy:
                        have_busy = True
                        t.busy(True)
                        customer.set_customer_status('table', t)
                        n = t.number
                        break
                if have_busy:
                    print(f'Посетитель номер {customer.number} сел за стол {n}. ')
                    self.to_out.put(customer)
                    sleep(5)
                else:
                    oldc = customer.status
                    customer.status = 'in queue'
                    self.waiting.put(customer)
                    if oldc!='in queue':
                        print(f'Посетитель номер {customer.number} ожидает свободный стол.')
                if self.waiting.qsize()>0:
                    customer = self.waiting.get()
                else:
                    customer = self.queue.get()

    def go_customer(self):
        if self.to_out.qsize()>0:
            custom = self.to_out.get()

            while custom:
                if custom.status=='table':
                    sleep(3)
                    custom.table.busy(False)
                    custom.set_customer_status('go', None)
                    print(f'Посетитель номер {custom.number} покушал и ушёл')
                    custom = self.to_out.get()

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
