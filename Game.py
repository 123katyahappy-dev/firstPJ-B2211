class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = []

    def attack(self, enemy):
        enemy.hp -= self.damage
        print(f"{self.name} attacks {enemy.name} for {self.damage} damage!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to inventory.")

    def show_inventory(self):
        print("\nInventory:")
        if len(self.inventory) == 0:
            print("Inventory is empty.")
        else:
            for item in self.inventory:
                print(f"- {item.name} (Value: {item.value})")


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, player):
        player.hp -= self.damage
        print(f"{self.name} attacks {player.name} for {self.damage} damage!")


# Creating player and enemy
player = Player("Hero", 100, 20)
enemy = Enemy("Goblin", 80, 15)

# Creating items
sword = Item("Sword", 100)
potion = Item("Health Potion", 50)

# Adding items to inventory
player.add_item(sword)
player.add_item(potion)

# Showing inventory
player.show_inventory()

# Battle system
print("\nBattle starts!\n")

while player.hp > 0 and enemy.hp > 0:
    player.attack(enemy)
    print(f"{enemy.name} HP: {enemy.hp}")

    if enemy.hp <= 0:
        print(f"\n{enemy.name} has been defeated!")
        break

    enemy.attack(player)
    print(f"{player.name} HP: {player.hp}")

    if player.hp <= 0:
        print(f"\n{player.name} has been defeated!")
        break