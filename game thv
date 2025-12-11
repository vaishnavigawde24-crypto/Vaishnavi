import in streamlit

# Base class for a character in the game (could be Dragon or King)
class Character:
    def __init__(self, name, health, power, defense, attack_type):
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
        self.attack_type = attack_type  # 'melee', 'ranged', or 'magic'
        self.level = 1
        self.experience = 0

    def attack(self, target):
        damage = self.calculate_damage(target)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def calculate_damage(self, target):
        base_damage = self.power
        # Calculate damage modifiers based on attack type and target defense
        if self.attack_type == 'melee':
            return max(0, base_damage - target.defense)
        elif self.attack_type == 'ranged':
            return max(0, base_damage - target.defense // 2)
        elif self.attack_type == 'magic':
            return max(0, base_damage - target.defense // 3)
        return base_damage

    def level_up(self):
        self.level += 1
        self.health += 20
        self.power += 5
        self.defense += 2
        self.experience = 0
        print(f"{self.name} has leveled up to level {self.level}!")

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:  # For simplicity, level up every 100 XP
            self.level_up()

# Dragon subclass
class Dragon(Character):
    def __init__(self, name, element, health, power, defense):
        super().__init__(name, health, power, defense, attack_type='magic')
        self.element = element

    def breathe_fire(self, target):
        damage = random.randint(10, 30) + self.power
        target.health -= damage
        print(f"{self.name} breathes fire at {target.name}, causing {damage} damage!")

# King subclass
class King(Character):
    def __init__(self, name, kingdom, health, power, defense):
        super().__init__(name, health, power, defense, attack_type='melee')
        self.kingdom = kingdom

    def swing_sword(self, target):
        damage = random.randint(5, 20) + self.power
        target.health -= damage
        print(f"{self.name} swings his sword at {target.name}, causing {damage} damage!")

# Battle function to simulate combat between two characters
def battle(character1, character2):
    print(f"\nBattle between {character1.name} and {character2.name}!\n")
    while character1.health > 0 and character2.health > 0:
        character1.attack(character2)
        if character2.health <= 0:
            print(f"{character2.name} has been defeated!")
            character1.gain_experience(50)
            break

        character2.attack(character1)
        if character1.health <= 0:
            print(f"{character1.name} has been defeated!")
            character2.gain_experience(50)
            break

    print(f"\nFinal Health: {character1.name}: {character1.health}, {character2.name}: {character2.health}\n")

# Example usage
dragon = Dragon(name="Flare", element="Fire", health=100, power=20, defense=10)
king = King(name="King Arthur", kingdom="Camelot", health=120, power=15, defense=15)

# Simulate a battle
battle(dragon, king)

# Output the final stats after battle
print(f"{dragon.name} - Health: {dragon.health}, Power: {dragon.power}, Level: {dragon.level}")
print(f"{king.name} - Health: {king.health}, Power: {king.power}, Level: {king.level}")
