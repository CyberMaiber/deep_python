# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import math


def add_and_multiply_fractions(fraction1, fraction2):
    # Разбиваем дроби на числитель и знаменатель
    num1, denom1 = fraction1.split('/')
    num2, denom2 = fraction2.split('/')

    # Вычисляем произведение
    product_num = int(num1) * int(num2)
    product_denom = int(denom1) * int(denom2)

    # Приводим знаменатели к общему знаменателю
    common_denom = int(denom1) * int(denom2)
    num1 = int(num1) * int(denom2)
    num2 = int(num2) * int(denom1)
    
    # Складываем числители
    sum_num = num1 + num2
    
    # Сокращаем дроби
    gcd = math.gcd(sum_num, common_denom)
    sum_num //= gcd
    common_denom //= gcd
    
    gcd = math.gcd(product_num, product_denom)
    product_num //= gcd
    product_denom //= gcd
    
    # Возвращаем результат в виде строки "a/b"
    sum_fraction = str(sum_num) + '/' + str(common_denom)
    product_fraction = str(product_num) + '/' + str(product_denom)
   
    return sum_fraction, product_fraction


fraction1 = "1/2"
fraction2 = "2/3"
sum_fraction, product_fraction = add_and_multiply_fractions(fraction1, fraction2)
print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", product_fraction)