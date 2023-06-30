# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

#РЕШЕНИЕ В date.py

from date import is_valid_date

date = input("Введите дату в формате DD.MM.YYYY: ")
if is_valid_date(date):
    print("Дата может существовать")
else:
    print("Дата не может существовать")