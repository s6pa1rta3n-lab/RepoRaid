import random

class Player:
    def __init__(self):
        # Initial values: Health = 100, Fuel = 50, Gold = 0, Oxygen = 100, XP = 0, Level = 1
        self.health = 100
        self.fuel = 50
        self.gold = 0
        self.items = []
        self.oxygen = 100
        self.xp = 0
        self.level = 1
    
    def check_status(self):
        # Displays current player status, show None if no items
        pass
    
    def level_up(self):
        # XP required to level up: 100; resets XP to 0 after leveling up and print appropriate message
        pass
    
    def use_oxygen(self):
        # Oxygen limit: 100; cannot use oxygen if supply is below 10 and print appropriate message
        pass
    
    def collect_gold(self, amount):
        # Collects gold and increment amount with appropriate message
        pass

class Alien:
    def __init__(self, name, health, attack):
        # Alien health typically ranges from 30 to 100; attack power ranges from 5 to 15
        self.name = name
        self.health = health
        self.attack = attack
    
    def attack_player(self, player):
        # Alien attack damage varies between 3 and its max attack power, reduce player health and show appropriate message
        pass
class SpaceGame:
    def __init__(self):
        # Initializes game with a player character
        self.player = Player()
    
    def start_game(self):
        # Displays game introduction and starts the main loop
        print("Welcome to the Space Exploration Adventure!")
        print("Travel across planets, meet aliens, and gather resources.")
        self.game_loop()
    
    def game_loop(self):
        # Runs the game loop until player health or fuel reaches 0
        while self.player.health > 0 and self.player.fuel > 0:
            action = self.main_menu()
            if action == "1":
                self.explore_planet()
            elif action == "2":
                self.player.check_status()
            elif action == "3":
                self.player.use_oxygen()
            elif action == "4":
                print("You decide to return to your home planet. Game Over.")
                break
    
    def main_menu(self):
        # Presents the main menu options to the player
        print("\nWhat would you like to do?")
        print("1. Explore a new planet")
        print("2. Check status")
        print("3. Use oxygen supply")
        print("4. Exit game")
        return input("Enter your choice: ")
    
    def explore_planet(self):
        # Randomly selects an event when exploring a new planet
        print("\nYou approach a new planet...")
        event = random.choice([self.alien_encounter, self.find_resources, self.empty_planet, 
                               self.fuel_station, self.asteroid_field, self.space_pirates, 
                               self.ancient_ruins, self.lost_colony, self.abandoned_ship, self.black_hole])
        event()
    
    def alien_encounter(self):
        # Creates a random alien encounter for combat, call create_alien() and combat() and display appropriate message
        pass
    
    def create_alien(self):
        # Defines possible alien enemies with varying stats
        aliens = [
            Alien("Martian", 30, 5),
            Alien("Venusian", 50, 8),
            Alien("Zorgon", 100, 15),
            Alien("Cybertronian", 40, 6),
            Alien("Void Entity", 70, 10)
        ]
        return random.choice(aliens)
    
    def combat(self, alien):
        # Combat loop: Player and alien take turns attacking until one is defeated, loot alien if you win and
        # print appropriate messages for each outcome
        pass
    
    def attack_alien(self, alien):
        # Player deals random damage between 5 and 15 to the alien; print appropriate message as well
        pass
    
    def loot_alien(self, alien):
        # Player loots between 10 and 50 gold from a defeated alien by calling collect_gold()
        pass
    
    def find_resources(self):
        # Player finds resources, adding between 5 and 50 gold by calling collect_gold()
        pass
    
    def fuel_station(self):
        # Fuel station restores between 5 and 20 fuel and print appropriate message
        pass
    
    def empty_planet(self):
        # display "This planet is barren. Nothing to see here."
        pass
    
    def asteroid_field(self):
        # display "You navigate through an asteroid field, avoiding collisions!"
        pass
    
    def space_pirates(self):
        # display "Pirates attack your ship! Will you fight or escape?"
        pass
    
    def ancient_ruins(self):
        # display "You discovered ancient alien ruins with hidden technology!"
        pass
    
    def lost_colony(self):
        # display "You find a lost human colony struggling to survive."
        pass
    
    def abandoned_ship(self):
        print("An abandoned spaceship drifts in the void. Do you explore it?")
    
    def black_hole(self):
        # display "A black hole is nearby! Will you attempt to study it or flee?"
        print("A black hole is nearby! Will you attempt to study it or flee?")

if __name__ == "__main__":
    game = SpaceGame()
    game.start_game()
