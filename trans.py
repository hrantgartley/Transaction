import datetime


class Customer:
    def __init__(self, full_name: str = "", age: int = 0):
        self.full_name = full_name
        self.age = age

    def __str__(self) -> str:
        return (
            f"Customer Name: {self.full_name}"
            f"Customer age: {self.age}"
        )

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.full_name

    def set_name(self, good_soup):
        self.full_name = good_soup

    def backup_print(self):
        print(f"Customer Name: {self.full_name}")
        print(f"Customer age: {self.age}")


class Invoice:
    def __init__(self, price: float, date: datetime.datetime, happy: bool):
        self.price = price
        self.subtotal = 0.0
        self.tax = .085
        self.happy = happy
        self.date = date
        self.list_items = []
        self.good_message = "Thank you for shopping"
        self.bad_message = "Sorry for the mistake but please come again"

    # TODO: implement the __str__ method
    def __str__(self) -> str:
        return (
            "Cost:"
        )

    def calculate_total(self):
        for i in range(len(self.list_items)):
            self.subtotal += self.list_items[i].price
            return self.subtotal * (1 + self.tax)

    def order_date(self):
        return datetime.datetime.now()

    def choose_msg(self):
        if self.happy:
            return self.good_message
        else:
            return self.bad_message

    def add_item(self, price: float, array: list):
        return array.append(price)


class Item(Invoice):
    def __init__(self, desc: str, price: float):
        self.desc = desc
        self.price = price

    def array_total(self, array: list):
        cost = 0.0
        for i in range(len(array)):
            cost += array[i]
        return cost

    def total_price(self):
        for i in range(len(self.list_items)):
            self.subtotal += self.list_items[i]
        return (self.subtotal * self.tax) + self.price
