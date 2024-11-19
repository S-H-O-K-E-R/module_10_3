import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            rand_dep = randint(50, 500)
            with self.lock:
                if self.balance <= 500:
                    self.balance += rand_dep
                print(f"Пополнение: {rand_dep}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            rand_take = randint(50, 500)
            print(f'Запрос на {rand_take}')
            with self.lock:
                if rand_take <= self.balance:
                    self.balance -= rand_take
                    print(f"Снятие: {rand_take}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            sleep(0.001)

bk = Bank()

 # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')