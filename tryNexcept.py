
result = None

try:
    x = int(input("Write number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Write the number!")
else:
    print("The number is:", result)
finally:
    print("Thank you for using this program!")

try:
    age = int(input("Write your age: "))
    if age < 0:
        raise ValueError("Your age can't be less than 0!")

    if age == 0:
        raise ValueError("Your age can't be equal to 0!")

    print("Ok")

except ValueError as e:
    print("Mistake:", e)

class BankAccount:
    def __init__(self, money):
        self.money = money

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Не можно снять минус!")
        if amount > self.money:
            raise ValueError("Недостаточно денег!")
        if amount == 0:
            raise ZeroDivisionError("У вас нет денег.")
        if amount > self.money:

            answer = input("Взять кредит? (y/n): ")

            if answer == "y":
                print("Кредит оформлен!")
                self.money = 0

            else:
                print("Операция отменена.")

        self.money -= amount
        print("Снято:", amount)
        print("Осталось:", amount)

    def add_money(self, amount):

        if amount <= 0:
            raise ValueError("Нельзя добавить меньше 0!")

        self.money += amount

        print("Баланс:", self.money)


account = BankAccount(100)

try:
    take = int(input("Сколько снять? "))
    account.withdraw(take)

except ValueError as e:
    print("Ошибка:", e)
