#Напишите код, который запрашивает число и сообщает является ли
#оно простым или составным. Используйте правило для проверки:
#“Число является простым, если делится нацело только на единицу и на себя”.
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Введите число от 1 до 100000: "))

if num <= 0 or num > 100000:
    print("Число должно быть от 1 до 100000")
elif num == 1:
    print("1 не является ни простым, ни составным числом")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "является простым числом")
    else:
        print(num, "является составным числом")