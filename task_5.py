revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

profit = revenue - costs
loss = costs - revenue

if revenue > costs:
    print('Фирма отработала с прибылью! Прибыль составила: ', profit)
    print('Рентабельность выручки составлет: ', profit / revenue)
    staff = int(input('Введите количество сотрудников фирмы: '))
    print('Прибыль фирмы в расчёте на одного сотрудника: ', profit / staff)
else:
    print('Фирма отработала с убытком( Убыток составил: ', loss)
