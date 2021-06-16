with open('text_3.txt', 'r', encoding='UTF-8') as f:
    surnames = []
    average_income = 0
    line_number = 0
    for line in f:
        line_number += 1
        surname, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            surnames.append(surname)
        average_income += income
    average_income /= line_number
print('Сотрудники, чей оклад менее 20 тысяч: ', surnames)
print(f"Средняя величина дохода сотрудников: {average_income:.2f}")
