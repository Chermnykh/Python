user_seconds=int(input('Введите время в секундах, а мы Вам преобразуем их в часы, минуты и секунды: '))

seconds = user_seconds % 60
minutes = (user_seconds // 60) % 60
hours = (user_seconds // 60) // 60
print(f"Время: {hours:02d}:{minutes:02d}:{seconds:02d}")
