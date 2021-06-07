def print_data(**kwargs):
    return ' '.join(kwargs.values())


print(print_data(name=input('Ваше имя: '),
surname=input('Ваша фамилия: '),
birth_year=input('Год рождения: '),
city=input('Город: '),
email=input('Email: '),
phone_number=input('Номер телефона: ')))
