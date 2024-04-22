import random
import time

class MiddleEarthAdventure:
    def __init__(self):
        self.locations = ["King County", "Snohomish County", "Pierce County", "Kitsap County", "Thurston County"]
        self.artifacts = ["One Lake", "One copy", "One (open)format", "One user experience", "One access control method",
                          "One security model", "One governance model", "One monitoring hub", "One licensing structure"]
        self.player_location = random.choice(self.locations)
        self.enemy = random.choice(["Bug", "Zero day", "Malware", "Feature", "Developer", "Manager", "Product Owner",
                                    "Release Train Engineer", "Devops", "MLops", "Scrum master"])
        self.health = 100
        self.inventory = []

    def display_intro(self):
        print("Welcome to Middle-earth Adventure!")
        print("You find yourself in the peaceful land of", self.player_location)
        print("Your quest is to defeat the enemy", self.enemy)
        print("You currently have", self.health, "health.")

    def explore(self):
        print("You begin your journey...")
        time.sleep(1)
        print("You venture deeper into Middle-earth...")
        time.sleep(1)
        print("You stumble upon a hidden treasure!")
        artifact_found = random.choice(self.artifacts)
        print("You found:", artifact_found)
        self.inventory.append(artifact_found)

    def battle(self):
        print("You encounter a fearsome", self.enemy, "!")
        time.sleep(1)
        print("A battle ensues...")
        enemy_health = random.randint(50, 100)
        while self.health > 0 and enemy_health > 0:
            player_attack = random.randint(10, 20)
            enemy_attack = random.randint(10, 25)
            print("You attack the enemy!")
            time.sleep(1)
            print("You deal", player_attack, "damage.")
            enemy_health -= player_attack
            if enemy_health <= 0:
                print("You defeated the", self.enemy, "!")
                print("You gain victory and continue your journey.")
                break
            print("The enemy attacks you!")
            time.sleep(1)
            print("The", self.enemy, "deals", enemy_attack, "damage.")
            self.health -= enemy_attack
            print("Your health:", self.health)
            time.sleep(1)
        if self.health <= 0:
            print("You have been defeated. Game over.")

    def display_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print("-", item)

    def play(self):
        self.display_intro()
        while self.health > 0:
            action = input("What would you like to do? (explore/battle/inventory/quit): ").lower()
            if action == "explore":
                self.explore()
            elif action == "battle":
                self.battle()
            elif action == "inventory":
                self.display_inventory()
            elif action == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please choose explore, battle, inventory, or quit.")

# Start the game
game = MiddleEarthAdventure()
game.play()
