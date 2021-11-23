#practice oop
class Calculator:
    @staticmethod
    def add(a1, a2):
        return a1 + a2

n1 = int(input())
n2 = int(input())
print(Calculator.add(n1, n2))