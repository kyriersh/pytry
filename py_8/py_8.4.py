# practice with oop
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, result):
        return (self.balance + result.balance)


a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result)