class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
        self.inventory = []

    def info(self):
        print(self.name, self.level, self.health)

    def rest(self):
        self.health += 10
        print(f"{self.name} rests (+10 HP)")

    def attack(self):
        print(f"{self.name} does a basic attack")


class Warrior(Character):
    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.stamina = 100

    def attack(self):
        if self.stamina >= 10:
            self.stamina -= 10
            print(f"{self.name} hits with sword (-10 stamina)")
        else:
            print(f"{self.name} is tired")


class Mage(Character):
    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.mana = 100

    def attack(self):
        if self.mana >= 15:
            self.mana -= 15
            print(f"{self.name} casts fireball (-15 mana)")
        else:
            print(f"{self.name} no mana")


class Archer(Character):
    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.energy = 100

    def attack(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} shoots arrow (-10 energy)")
        else:
            print(f"{self.name} tired")


class EliteWarrior(Warrior):
    def attack(self):
        print(f"{self.name} uses ULTIMATE SLASH 💥")


heroes: list[Character] = [
    Warrior("Ragnar", 5, 120),
    Mage("Merlin", 7, 80),
    Archer("Robin", 6, 90),
    EliteWarrior("Thor", 10, 200)
]

for h in heroes:
    h.info()
    h.attack()
    h.rest()

print("\nInventory:")
heroes[0].inventory.append("Sword")
heroes[1].inventory.append("Staff")
heroes[2].inventory.append("Bow")

for h in heroes:
    print(h.name, ":", h.inventory)