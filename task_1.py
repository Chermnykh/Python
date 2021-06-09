from sys import argv

script_name, production, rate, bonus = argv

print('Имя скрипта: ', script_name)
print('Выработка в часах: ', production)
print('Ставка в час: ', rate)
print('Премия: ', bonus)
print('Заработная плата: ', (float(production) * float(rate)) + float(bonus))
