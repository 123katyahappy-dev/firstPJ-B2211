# papa

class Character:
    def __init__(self, name, level, hp, damage):
        self.name = name
        self.level = level
        self.hp = hp
        self.damage = damage

    def attack(self):
        return self.level

    def defend(self, damage):
        self.hp -= self.damage

    def status(self):
       print(self.name, self.level, self.hp)

#children

class Warrior(Character):
   def attack(self):
       return self.level * 3

   def defend(self, damage):
       self.hp -= damage

class Mage(Character):
    def attack(self):
        return self.level * 4
    def defend(self, damage):
        self.hp -= damage

class Scout(Character):
    def attack(self):
        return self.level * 2
    def defend(self, damage):
        self.hp -= damage

#team

class Team:
    def __init__(self):
        self.members = []

    def add_member(self, character):
        self.members.append(character)

    def remove_member(self, character):
        self.members.remove(character)

    def total_power(self):
        total = 0
        for member in self.members:
            total += member.attack()
        return total

    def find_strongest(self):
        strongest = self.members[0]
        if not self.members:
            return None

        for member in self.members:
            if member.attack() > strongest.attack():
                strongest = member
        return strongest

    def show_team(self):
        for member in self.members:
            member.status()



class Arena:
    def battle(self, char1, char2):
        round_num = 1

        while char1.hp > 0 and char2.hp > 0:
            print("Round", round_num)

            damage = char1.attack()
            char2.defend(damage)

            if char2.hp <= 0:
                print(char1.name, "won!")
                return char1

            damage = char2.attack()
            char1.defend(damage)

            if char1.hp <= 0:
                print(char2.name, "won!")
                return char2

            round_num += 1


print("START")

arena = Arena()

w = Warrior("Bob", 100, 140, 15)
m = Mage("Alice", 80, 120, 17)

winner = arena.battle(w, m)

print("END")
print("Winner:", winner.name)
