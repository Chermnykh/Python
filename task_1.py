import itertools, time


class TrafficLight:
    def __init__(self):
        self.__states_colors = ['Красный', 'Желтый', 'Зеленый']
        self.__color = None
        self.__previous_color = None
        self.__states = itertools.cycle(self.__states_colors)

    def running(self):
        while True:
            if self.__color is None:
                self.__color = self.__states.__next__()
                print('\r' + self.__color, end = '')
            elif self.__color == 'Красный':
                if self.__previous_color != "Зеленый" and self.__previous_color != None:
                    print('Неверный порядок')
                    return 1
                self.__previous_color = self.__color
                time.sleep(7)
                self.__color = self.__states.__next__()
                print('\r' + self.__color, end = '')
            elif self.__color == 'Желтый':
                if self.__previous_color != "Красный" and self.__previous_color != None:
                    print('Неверный порядок')
                    return 1
                self.__previous_color = self.__color
                time.sleep(2)
                self.__color = self.__states.__next__()
                print('\r' + self.__color, end = '')
            elif self.__color == 'Зеленый':
                if self.__previous_color != "Желтый" and self.__previous_color != None:
                    print('Неверный порядок')
                    return 1
                self.__previous_color = self.__color
                time.sleep(5)
                self.__color = self.__states.__next__()
                print('\r' + self.__color, end = '')


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()
