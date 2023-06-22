# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

balance = 0  # Баланс на карте. Стартовый баланс 0.
count = 0  # Количество операций
# tax = 0 #Налог
log_list = [] # список операций пополнения/снятия

def reach_tax():
    global balance
    if balance > 5000000:  # Налог на богатство
        tax = balance * 0.1
        balance -= tax


def third_operation_percent():
    global count
    global balance
    if count % 3 == 0:  # Начисление процентов за каждую третью операцию
        balance += balance * 0.03


while True:
    print("1. Пополнить")
    print("2. Снять")
    print("3. Выйти")
    choice = int(input("Выберите действие: "))

    if choice == 1:
        reach_tax()
        amount = int(input("Введите сумму для пополнения (кратную 50): "))
        if amount % 50 != 0:
            print("Сумма должна быть кратна 50")
            continue
        balance += amount
        log_list.append(f"Пополнение баланса: {amount}")
        count += 1
        third_operation_percent()

        print("Баланс: ", balance)

    elif choice == 2:
        reach_tax()
        amount = int(input("Введите сумму для снятия (кратную 50): "))
        if amount % 50 != 0:
            print("Сумма должна быть кратна 50")
            continue
        if amount > balance:
            print("Недостаточно средств")
            continue
        fee = max(amount * 0.015, 30)  # Комиссия за операцию
        if fee > 600:
            fee = 600
        balance -= amount + fee
        log_list.append(f"Списание с баланса: {amount}")
        count += 1
        third_operation_percent()

        print("Баланс: ", balance)

    elif choice == 3:
        break

    else:
        print("Неверный выбор")
        continue

print ("Список операций:")
print (log_list)