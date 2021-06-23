from abc import ABC, abstractmethod, abstractproperty


class Clothes(ABC):

    @abstractmethod
    def expense(self):
        pass

    @abstractproperty
    def title(self):
        return "Parent class"


class Coat(Clothes):
    def __init__(self, title, size):
        self.size = size
        self.title_name = title

    @property
    def title(self):
        return self.title_name

    @property
    def expense(self):
        return round((self.size / 6.5) + 0.5, 2)


class Suit(Clothes):
    def __init__(self, title, height):
        self.height = height
        self.title_name = title

    @property
    def title(self):
        return self.title_name

    @property
    def expense(self):
        return round(self.height * 2 + 0.3, 2)


coat_fabric = Coat('Пальто', 48)
print('Расход ткани на пальто:', coat_fabric.expense)
suit_fabric = Suit('Костюм', 165)
print('Расход ткани на костюм:', suit_fabric.expense)

clothes = [coat_fabric, suit_fabric]
print('Общий расход ткани:', sum(map(lambda x: x.expense, clothes)))
