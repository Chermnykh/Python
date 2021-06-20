class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_road_weight(self, weight, height):
        return self._length * self._width * weight * height

road = Road(5000, 20)
print(road.calculate_road_weight(25, 5))
