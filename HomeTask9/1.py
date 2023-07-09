# Напишите следующие функции:
# ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import math
import csv
import random
import json
import os


def generate_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(random.randint(100, 1000)):
            row = [random.randint(-10, 10) for _ in range(3)]
            writer.writerow(row)


def equation_deco(func):
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
    return wrapper


def save_to_json_deco(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        data = {
            "a": a,
            "b": b,
            "c": c,
            "korni": result
        }
        print(f"Уравнение: {a}*x^2 + {b}*x + {c} = 0")
        print(f"Корни: {result}")
        print()
        with open("results.json", 'a', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)
            jsonfile.write('\n')
    return wrapper


@equation_deco
@save_to_json_deco
def solve_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Beskonechnoe mnozhestvo resheniy"
            else:
                return "Net resheniy"
        else:
            x = -c / b
            return x
    else:
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return x1, x2
        elif discriminant == 0:
            x = -b / (2*a)
            return x
        else:
            return "Net veschestvennih korney"


os.chdir('HomeTask9')
generate_csv("numbers.csv")
solve_equation("numbers.csv")
