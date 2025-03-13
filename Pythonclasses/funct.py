import random


# Define the Player class
class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


# Define the Enemy class
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


# Combat mechanics
def attack(attacker, defender):
    damage = max(0, attacker.attack - defender.defense)
    print(f"{attacker.name} attacks {defender.name} for {damage} damage!")
    defender.take_damage(damage)


# Display the status of the player and enemy
def show_status(player, enemy):
    print(f"\n{player.name} (HP: {player.health}) vs. {enemy.name} (HP: {enemy.health})\n")


# Main function for the game
def game():
    print("Welcome to the Text-Based RPG Game!")

    # Player creation
    name = input("Enter your character's name: ")
    player = Player(name, health=100, attack=15, defense=5)

    # Enemy creation
    enemy = Enemy(name="Goblin", health=50, attack=10, defense=3)

    # Main game loop
    while player.is_alive() and enemy.is_alive():
        show_status(player, enemy)

        # Player's turn
        print("Choose an action:")
        print("1. Attack")
        print("2. Defend")
        action = input("Enter the number of your choice: ")

        if action == "1":
            attack(player, enemy)
        elif action == "2":
            print(f"{player.name} defends!")
            player.defense += 3  # Temporary defense boost for the turn
        else:
            print("Invalid choice. You lose your turn.")

        if enemy.is_alive():
            # Enemy's turn
            print(f"\n{enemy.name}'s turn!")
            attack(enemy, player)
            # Reset player defense after turn if they defended
            if action == "2":
                player.defense -= 3

    # Game over message
    if player.is_alive():
        print(f"\n{player.name} wins the battle!")
    else:
        print(f"\n{player.name} has been defeated. Game over!")


if __name__ == "__main__":
    game()
