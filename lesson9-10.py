class Hero:
    def __init__(self, name):

        self.name = name

        self.hp = 100
        self.mana = 50
        self.level = 1
        self.inventory = []

    def attack(self):

        print(self.name, "Attack!")

    def heal(self):

        print(self.name, "Heal!")

hero = Hero("Hero")

print(dir(hero))
print(type(hero))

if isinstance(hero, Hero):
    print("I`m a Hero!")

class Mage(Hero):

  def __init__(self, name, mana: int, level: int):
    super().__init__(name)
    self.mana = mana
    self.level = level
    self.inventory = []

  def magic_cane(self):

        print(self.name, "Magic is here!")

  def magic_heal(self):
        print(self.name, "Heal my friends!")

mage = Mage(name="Georgiy", mana=50, level=1)

mage.magic_cane()
mage.magic_heal()
if (isinstance(mage, Mage)):
    print("I`m a Mage!")

if (isinstance(mage, Hero)):
    print("I`m a Hero!")

mana = getattr(mage,"mana")

print(mana)

level = getattr(hero,"level")

print(level)

setattr(Hero,"Level", 10)

print(getattr(Hero,"Level"))

if mage.level > 5:
    setattr(mage, "mana", mage.mana + 20)

setattr(hero, "inventory", [])

hero.inventory.append("Potion")
hero.inventory.append("Bow")

print(hero.inventory)

if hasattr(hero, "inventory"):
    print("There are some items in your inventory!")

print(hasattr(hero, "mana"))
delattr(hero, "mana")
print(hasattr(hero, "mana"))

print(hero.__dict__)





