# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

class Bankomat:
    def __init__(self):
        self.balance = 0
        self.operations_count = 0
    
    def deposit(self, amount):
        self.check_reach()
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратна 50 у.е.")
            return
        
        self.balance += amount
        self.operations_count += 1
        self.calculate_interest()
        self.print_balance()
    
    def withdraw(self, amount):
        self.check_reach()
        if amount % 50 != 0:
            print("Сумма снятия должна быть кратна 50 у.е.")
            return

        if amount > self.balance:
            print("Недостаточно средств на счете")
            return
        
        withdrawal_fee = min(max(amount * 0.015, 30), 600)
        self.balance -= amount + withdrawal_fee
        self.operations_count += 1
        self.calculate_interest()
        self.print_balance()
    
    def check_reach(self):
        if self.balance >= 5000000:
            self.balance -= self.balance * 0.1
            print(f"Налог на роскошь: {self.balance * 0.1} у.е.")

    def calculate_interest(self):
        if self.operations_count % 3 == 0:
            interest = self.balance * 0.03
            self.balance += interest
    
    def print_balance(self):
        print(f"Доступная сумма на счете: {self.balance} у.е.")
    
    # def close_account(self):
    #     self.balance = 0
    #     self.operations_count = 0
    #     print("Банковский счет закрыт")


account = Bankomat()
while True:
    print("1. Пополнить")
    print("2. Снять")
    print("3. Выйти")
    choice = int(input("Выберите действие: "))

    if choice == 1:
        amount = int(input("Введите сумму для пополнения (кратную 50): "))
        account.deposit(amount)
    elif choice == 2:
        amount = int(input("Введите сумму для снятия (кратную 50): "))
        account.withdraw(amount)
    elif choice == 3:
        break
    else:
        print("Неверный выбор")
        continue