class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print('Машина повернула {}'.format(direction))

    def show_speed(self):
        print('Скорость автомобиля:', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('ПРЕВЫШЕНА СКОРОСТЬ!!!')
            print('Скорость автомобиля:', self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('ПРЕВЫШЕНА СКОРОСТЬ!!!')
            print('Скорость автомобиля:', self.speed)

class PoliceCar(Car):
    pass

town_car = TownCar(120, 'Black', 'Mazda', False)
print('Town Car:')
town_car.show_speed()
town_car.go()
sport_car = SportCar(0, 'Black', 'Lexus', False)
print('\n''Sport Car:')
sport_car.stop()
work_car = WorkCar(41, 'Red', 'Ford', False)
print('\n''Work Car:')
work_car.show_speed()
work_car.turn('налево')
police_car = PoliceCar(60, 'Black', 'Mazda', True)
print('\n''Police Car:')
police_car.turn('направо')
