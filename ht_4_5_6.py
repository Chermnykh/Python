import uuid


class MyError(Exception):
    pass


def funk_retry(funk, args=tuple(), argv=dict(), tries=3):
    for i in range(tries):
        try:
            res = funk(*args, **argv)
            return res
        except Exception as e:
            print(e)
            print('Введенный тип данных неверен. Осталось попыток: {}'.format(tries - i - 1))
            continue
    raise MyError


def raise_value_error():
    raise ValueError


def check_f1(field):
    if not field.isalpha():
        raise ValueError
    else:
        return field


def check_f2(field):
    if not field.isdigit():
        raise ValueError
    else:
        return field


def check_f3(field):
    if not field.isdigit():
        raise ValueError
    else:
        return field


def wrapper(checker, prompt):
    field = input(prompt)
    field = checker(field)
    return field


def check_f4(field):
    if not field.isdigit():
        raise ValueError
    if int(field) not in [1, 2, 3]:
        raise ValueError
    else:
        return int(field)


class Warehouse:
    def __init__(self):
        self.SENT = 'Sent'
        self.APPLIED = 'Apply'
        self.devices = dict()
        self.log = list()
        self.PRINTER = 1
        self.SCANNER = 2
        self.XEROX = 3
        self.device_assemblers = {
            self.PRINTER: Printer,
            self.SCANNER: Scanner,
            self.XEROX: Xerox
        }

    def send_item(self, device_id, office_id):
        self.log.append([device_id, self.SENT, office_id])
        self.devices.pop(device_id)

    def add_items(self):
        try:
            while True:
                eq_type = funk_retry(wrapper, args=(check_f4, "ENTER TYPE: 1: Принтер 2: Сканер 3: Ксерокс \n"),
                                     tries=3)
                item = self.device_assemblers[eq_type]()
                check_more_items = input('Хотите продолжить? (Y/N): ')
                self.add_item(item)
                if check_more_items.lower() == 'y':
                    continue
                else:
                    break
        except MyError:
            print("Попыток больше нет")

    def add_item(self, item):
        id = str(uuid.uuid4())
        self.devices[id] = item
        self.log.append([id, self.APPLIED, 'Склад'])

    def info(self):
        for i in self.devices:
            print(self.devices[i])
        return self.devices


class OfficeEquipment:
    def __init__(self):
        self.name = funk_retry(wrapper, args=(check_f1, 'Название: '), tries=3)
        self.price = funk_retry(wrapper, args=(check_f2, 'Цена: '), tries=3)
        self.color = funk_retry(wrapper, args=(check_f1, 'Цвет: '), tries=3)


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.printer_type = funk_retry(wrapper, args=(check_f1, 'Тип принтера: '), tries=3)

    def __str__(self):
        return f'ПРИНТЕР: \tНазвание: {self.name}, \tЦена: {self.price}, \tЦвет: {self.color}, \tТип принтера: ' \
               f'{self.printer_type}'


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.scanner_sensor = funk_retry(wrapper, args=(check_f1, 'Тип сенсора: '), tries=3)

    def __str__(self):
        return f'СКАНЕР: \tНазвание: {self.name}, \tЦена: {self.price}, \tЦвет:{self.color}, \tТип сенсора: ' \
               f'{self.scanner_sensor}'


class Xerox(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.xerox_wifi = funk_retry(wrapper, args=(check_f1, 'Wi-fi: '), tries=3)

    def __str__(self):
        return f'КСЕРОКС: \tНазвание: {self.name}, \tЦена: {self.price}, \tЦвет:{self.color}, \tWi-fi: ' \
               f'{self.xerox_wifi}'


wh = Warehouse()
wh.add_items()

wh.info()
print('Один продукт был отправлен на склад: ')
wh.send_item(list(wh.devices.keys())[0], '')
wh.info()
