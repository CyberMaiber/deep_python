#Программа загадывает число от 0 до 1000.
#Необходимо угадать число за 10 попыток.
#Программа должна подсказывать «больше» или «меньше» после каждой попытки.

import random

number = random.randint(0, 1000)
guesses_left = 10

print("Угадайте число от 0 до 1000. У вас есть 10 попыток.")

while guesses_left > 0:
    guess = int(input("Введите вашу догадку: "))
    guesses_left -= 1
    
    if guess == number:
        print("Поздравляем! Вы угадали число!")
        break
    elif guess < number:
        print("Загаданное число больше вашей догадки.")
    else:
        print("Загаданное число меньше вашей догадки.")
        
    if guesses_left > 0:
        print("У вас осталось", guesses_left, "попыток.")
    else:
        print("У вас не осталось попыток. Загаданное число было", number)