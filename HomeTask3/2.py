
# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

# Функция принимает список и возвращает список дублирующихся элементов
def find_duplicates(lst):  
    duplicates = []
    for i in lst:
        if lst.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates

# Пример использования
my_list = [1, 2, 3, 4, 5, 2, 3, 6, 8, 7, 9, 9]
print(find_duplicates(my_list)) 