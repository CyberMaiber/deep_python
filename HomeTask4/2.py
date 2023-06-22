# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def get_arguments(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not hashable(key):
            key = str(key)
        result[value] = key
    return result

def hashable(obj):
    try:
        hash(obj)
    except TypeError:
        return False
    return True

result = get_arguments(a=1, bed_value=22, c="hello")
print(result)
