from threading import Lock,Thread
lck = Lock()
class BankAccount:
  def __init__(self, sum):
    self.summ = sum
  def deposit(self,amount):
    with lck:
      self.summ+= amount
    print(f'Deposited {amount}, new balance is {self.summ}')
  def withdraw(self, amount):
    with lck:
      self.summ-= amount
    print(f'Withdrew {amount}, new balance is {self.summ}')

def deposit_task(account, amount):
  for _ in range(5):
    account.deposit(amount)

def withdraw_task(account, amount):
  for _ in range(5):
    account.withdraw(amount)
account = BankAccount(1000)

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()