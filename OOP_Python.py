class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.knowledge = 50

    def study(self):
        print("Студент учится")
        self.knowledge += 10

    def work(self):
        print("Студент работает")
        self.money += 50

    def rest(self):
        print("Студент отдыхает")
        self.money -= 20

    def live_one_day(self):
        print("\nНовый день")

        if self.money < 20:
            print("Нужно заработать денег")
            self.work()

        elif self.knowledge < 40:
            print("Нужно учиться")
            self.study()

        else:
            print("Можно отдохнуть")
            self.rest()

        print("Деньги:", self.money)
        print("Знания:", self.knowledge)


student = Student("Андрей")

for day in range(365):
    print(f"\nДень {day + 1}")
    student.live_one_day()
