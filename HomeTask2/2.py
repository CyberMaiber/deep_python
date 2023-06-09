# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

def to_hex(num):
    hex_chars = "0123456789ABCDEF"
    hex_string = ""
    while num > 0:
        remainder = num % 16
        hex_string = hex_chars[remainder] + hex_string
        num //= 16
    return hex_string

# Пример использования
num = int(input("Введите целое число: "))
hex_string = to_hex(num)
print(hex_string)
print(hex(num))