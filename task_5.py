class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Я ручка! Мной пишут.')

class Pencil(Stationery):
    def draw(self):
        print('Я карандаш! Мной рисуют.')

class Handle(Stationery):
    def draw(self):
        print('Я маркер! Мной тоже могут рисовать!')


stationery = Stationery("Канцелярские принадлежности")
stationery.draw()
pen = Pen("Ручка")
print(pen.title)
pen.draw()
pencil = Pencil("Карандаш")
print(pencil.title)
pencil.draw()
handle = Handle("Маркер")
print(handle.title)
handle.draw()
