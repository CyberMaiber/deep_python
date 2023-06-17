# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей

# Создаем словарь с вещами каждого друга
friends = {
    'Вася': ('палатка', 'спальник', 'фонарик', 'нож'),
    'Петя': ('палатка', 'спальник', 'газовая горелка', 'кастрюля'),
    'Коля': ('палатка', 'сральник', 'коврик', 'карта')
}

# Находим одинаковые вещи у всех друзей
common_items = set.intersection(*[set(items) for items in friends.values()])
print('Одинаковые вещи у всех друзей:', common_items)

# Находим уникальные вещи у каждого друга
unique_items = set()
all_items = set()
for friend, items in friends.items():
    for item in items:
        if item in all_items:
            unique_items.discard(item)
        else:
            all_items.add(item)
            unique_items.add(item)

print('Все вещи:', all_items)
print('Вещи, которые есть только у одного друга:', unique_items)

# Находим вещи, которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
common_items = set(all_items)
# common_items_copy = common_items.copy()
for item in common_items.copy():
    counter = 0
    for friend, items in friends.items():
        if item not in items:
            counter += 1
    if not counter == 1: 
        common_items.discard(item)
print('Вещи, которые есть у всех друзей кроме одного:', common_items)

for friend, items in friends.items():
    for item in common_items:
        if item not in items:
            print('Вещь', item, 'отсутствует у друга', friend)

