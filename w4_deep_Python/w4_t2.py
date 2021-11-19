class Value:
    def __init__(self):
        self.amount = None

    def __get__(self, obj, owner):
        return self.amount

    def __set__(self, obj, value):
        self.amount = (1 - obj.commission) * value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
