class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.health = 100

    def info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("HP:", self.health)

    def sound(self):
        print(self.name, "Животное издаёт звук")

animal = Animal("Шульгур", 5)

animal.info()


class Dog(Animal):
    def __init__(self, name, age, strength):

        super().__init__(name, age)

        self.strength = strength

    def sound(self):
        print(self.name, "Собака гавкает")

    def info(self):

        super().info()

        print("Сила:", self.strength)


dog = Dog("Тузик", 5, 20)

dog.info()

print("Сила:", dog.strength)

class Fish(Animal):
    def __init__(self, name, age, intelligence):

        super().__init__(name, age)

        self.intelligence = intelligence

    def sound(self):
        print(self.name, "Рыба булькает")

    def info(self):

        super().info()

        print("Разум:", self.intelligence)


fish = Fish("Колто", 1, 10)

fish.info()

class Hamster(Animal):
    def __init__(self, name, age, hunger):

        super().__init__(name, age)

        self.hunger = hunger

    def sound(self):
         print(self.name, "Хомяк пищит")

    def info(self):

        super(). info()

        print("Голод:", self.hunger)

hamster = Hamster("Коля",  "1",  "2")

hamster.info()

class WildAnimal (Animal):
    def __init__(self, name, age, danger):
        super().__init__(name, age)
        self.danger = danger

    def attack(self):

        print(self.name, "Атакует")

class Predator(WildAnimal):
    def __init__(self, name, age, danger):
        super().__init__(self, name, age)
        self.danger = danger

    def attack(self):

        print(self.name, "Атакует")

class Lion(Predator):
    def __init__(self, name, age, danger):
        super().__init__(name, age, danger)
        self.roar_power = 100

    def sound(self):

        print(self.name, "Громко рычит")

class Wolf(Predator):
    def __init__(self, name, age, danger):
        super().__init__(name, age, danger)
        self.roar_power = 100

    def sound(self):

        print(self.name, "Громко рычит")

class Tiger(Predator):
    def __init__(self, name, age, danger):
        super().__init__(name, age, danger)
        self.roar_power = 100

    def sound(self):

        print(self.name, "Громко рычит")

class Herbivorous(WildAnimal):
    def __init__(self, name, age, grass):
        super().__init__(name, age, grass)
        self.food = [100]

    def sound(self):
        print(self.name, "Yummy!")

class Hare(Herbivorous):
    def __init__(self, name, age, grass):
        super().__init__(self, name, age, grass)
        self.food = [100]

    def sound(self):
        print(self.name, "Yummy!")


class Deer(Herbivorous):
    def __init__(self, name, age, grass):
        super().__init__(self, name, age, grass)
        self.food = [200]

    def sound(self):
        print(self.name, "Yummy!")

class Wildebeest(Herbivorous):
    def __init__(self, name, age, grass):
        super().__init__(self, name, age, grass)
        self.food = [100]

    def sound(self):
        print(self.name, "Yummy!")

