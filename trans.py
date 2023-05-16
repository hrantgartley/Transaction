class Customer:
    def __init__(self, First='', Last='', PhoneNumber=''):
        self.First = First
        self.Last = Last
        self.PhoneNumber = PhoneNumber

    def PrintUserData(self):
        print(f"User's Name: {self.First} {self.Last}")
        print(f"User Phone: {self.PhoneNumber}")

    def __str__(self) -> str:
        return f'User\'s Name: {self.First} {self.Last}\nUser Phone: {self.PhoneNumber}'