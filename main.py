class User:
    def __init__(self, adult_count, child_count, price):
        self.adult_count = adult_count
        self.child_count = child_count
        self.price = price

    def get_total_price(self):
        total_price = self.count * self.price

class Adult(User):
    def __init__(self, count, price):
        super().__init__(count, price)

class Child(User):
    def __init__(self, count, price):
        super().__init__(count, price)


adult_count = int(input('大人の人数を教えてください'))

child_count = int(input('子供の人数を教えてください'))


