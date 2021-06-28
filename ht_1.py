import datetime


class Date:
    day = None
    month = None
    year = None

    def __init__(self, your_date):
        Date.your_date = datetime.datetime.strptime(your_date, "%Y-%m-%d")
        Date.day = Date.your_date.day
        Date.month = Date.your_date.month
        Date.year = Date.your_date.year

    @classmethod
    def take_date(cls):
        return tuple(map(int, [cls.day, cls.month, cls.year]))

    @staticmethod
    def valid_date(your_date):
        try:
            datetime.datetime.strptime(your_date, "%Y-%m-%d")
            return "Date is valid"
        except ValueError:
            return "Date is invalid"


d = '2016-2-23'
print(Date.valid_date(d))
if Date.valid_date(d) == 'Date is valid':
    date = Date(d)
    print(date.take_date())
