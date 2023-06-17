# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

# Создаем словарь со списком вещей и их массой
items = {
    "спальник": 1.5,
    "палатка": 3.0,
    "коврик": 0.5,
    "горелка": 0.3,
    "кухонная посуда": 1.0,
    "еда": 2.0,
    "вода": 2.5,
    "лопата": 1.0
}

# Максимальная грузоподъемность рюкзака
max_weight = 5.0

# Функция для нахождения всех возможных вариантов комплектации рюкзака
def find_combinations(items, max_weight):
    combinations = [[]]
    for item in items:
        new_combinations = []
        for combination in combinations:
            if sum([items[i] for i in combination]) + items[item] <= max_weight:
                new_combinations.append(combination + [item])
        combinations += new_combinations
    return combinations[1:]

# Находим все возможные варианты комплектации рюкзака
combinations = find_combinations(items, max_weight)

# Выводим результаты
print("Возможные варианты комплектации рюкзака:")
for combination in combinations:
    print(", ".join(combination), sum([items[i] for i in combination]))

print("\nВозможные варианты комплектации рюкзака с условием максимальной грузоподъемности:")
for combination in combinations:
    if sum([items[i] for i in combination]) == max_weight:
        print(", ".join(combination), sum([items[i] for i in combination]))

