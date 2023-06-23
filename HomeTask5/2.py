# Напишите однострочный генератор словаря, который принимает на вход три 
# списка одинаковой длины: имена str, ставка int, премия str с указанием 
# процентов вида «10.25%». В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии

names = ['Alice', 'Bob', 'Steve']
rates = [1000, 2000, 1500]
bonuses = ['10.25%', '5%', '7.5%']

result = {name: rate * float(bonus.rstrip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}
print(result)