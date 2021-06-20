class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

position = Position('Jony', 'Margulis', 'Art-designer', 934984, 7424)
print('Имя Фамилия:', *position.get_full_name())
print('Должность:', position.position)
print('Доход:', position.get_total_income())
