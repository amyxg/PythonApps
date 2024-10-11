# -*- coding: utf-8 -*-

"""
This program allows a user to play a fun game, runs on python OOP
m3pro game
10/8/2024
Amy Santjer

"""


from m3pro_class import Character, Player, Dragon, FireDragon, IceDragon, ElderDragon

class Room:
    """
    Represents a room in the dungeon.
    """
    def __init__(self, description): # desription: str
        self.__description = description
        self.__enemy = None
        self.__item = None

    def add_enemy(self, enemy):
        """
        Adds an enemy to the room.

        enemy: Dragon
        """
        self.__enemy = enemy

    def add_item(self, item):
        """
        Adds an item to the room.

        item: str
        """
        self.__item = item

    def get_description(self):
        """
        Returns the room description.
        
        """
        return self.__description

    def get_enemy(self):
        """
        Returns the enemy in the room.
        
        """
        return self.__enemy

    def get_item(self):
        """
        Returns the item in the room.
        
        """
        return self.__item

    def remove_item(self):
        """
        Removes the item from the room.
        
        """
        self.__item = None

class Game:
    """
    Manages the game flow and interactions.
    
    """
    def __init__(self):
        self.__player = None
        self.__rooms = []
        self.__current_room = 0

    def create_player(self, name):
        """
        Creates a new player character.
        
        name: str
        """
        self.__player = Player(name)

    def create_rooms(self):
        """
        Initializes the dungeon rooms.
        """
        # list of strings, each describing diff rooms
        room_descriptions = [
            "A dark cave entrance with claw marks on the walls",
            "A heated corridor with scorch marks",
            "A grand hall with frozen pillars",
            "A small treasure room filled with glittering scales",
            "The lair of the Elder Dragon"
        ]
        for desc in room_descriptions:
            self.__rooms.append(Room(desc))

        # Add dragons and items to rooms
        self.__rooms[1].add_enemy(FireDragon())
        self.__rooms[2].add_enemy(IceDragon())
        self.__rooms[3].add_item("Health Potion")
        self.__rooms[4].add_enemy(ElderDragon())

    def play(self):
        """
        Main game loop.
        """
        print("Welcome to the Dragon's Dungeon!")
        player_name = input("Enter your dragon slayer's name: ")
        self.create_player(player_name)
        self.create_rooms()

        # while loop to keep game going if player is alive 
        while self.__player.is_alive() and self.__current_room < len(self.__rooms):
            self.process_room()

        if self.__player.is_alive():
            print("\nCongratulations! You've conquered the Dragon's Dungeon!")
        else:
            print("\nGame Over. Your dragon slayer has been defeated!")

    def process_room(self):
        """
        Handles events in the current room.
        """
        room = self.__rooms[self.__current_room] # get and set room by room desc
        print(f"\n{room.get_description()}")

        enemy = room.get_enemy() # input enemy (dragon) in room and battle
        if enemy:
            self.combat(enemy)
        
        item = room.get_item() # input item in room and put in inventory
        if item and self.__player.is_alive():
            print(f"\nYou found a {item}!")
            self.__player.add_to_inventory(item)
            room.remove_item()

        if self.__player.is_alive():
            self.player_action()

    def combat(self, enemy):
        """
        Manages combat between player and dragon.
        
        enemy: Dragon
        """
        print(f"A {enemy.get_name()} appears!")
        
        # If the enemy is a dragon, it uses its special ability
        if isinstance(enemy, Dragon):
            print(f"The {enemy.get_name()} {enemy.special_ability()}!") # e.g IceDragon, using frost breath

        # while loop of enemy and player fighting until one dies
        while enemy.is_alive() and self.__player.is_alive():
            # Player's turn
            player_damage = self.__player.attack()
            enemy.take_damage(player_damage)
            print(f"You deal {player_damage} damage to the {enemy.get_name()}.")

            if enemy.is_alive():
                # Enemy's turn
                enemy_damage = enemy.attack()
                self.__player.take_damage(enemy_damage)
                print(f"The {enemy.get_name()} deals {enemy_damage} damage to you.")
            
            self.__player.display_stats()
            enemy.display_stats()

        if self.__player.is_alive():
            print(f"\nYou defeated the {enemy.get_name()}!")
            loot = enemy.drop_loot() # get 1 item from list containing multiple items for player
            if loot != "None":
                print(f"The {enemy.get_name()} dropped: {loot}")
                self.__player.add_to_inventory(loot)
            self.__player.gain_exp(enemy.get_exp_reward()) # gain exp points after each battle with enemy

    def player_action(self):
        """
        Handles player actions between rooms.
        """

        # while loop for player to conduct action (before each advancement to room / after battle)
        while True:
            action = input("\nWhat would you like to do? (move/use item/display stats/quit): ").lower()
            if action == "move":
                self.__current_room += 1
                break
            elif action == "use item":
                self.use_item()
            elif action == "display stats":
                self.__player.display_stats()
            elif action == "quit":
                print("\nThanks for playing!")
                exit()
            else:
                print("Invalid action. Please try again.") # exception handling to ensure user input available options

    def use_item(self):
        """
        Allows the player to use an item from their inventory.
        """
        if not self.__player.get_inventory():
            print("\nYour inventory is empty!")
            return

        print("\nYour inventory:", self.__player.get_inventory())
        item = input("Which item would you like to use? ")
        try:
            self.__player.use_item(item)
        except ValueError as e:
            print(str(e))

def main():
    """
    Entry point of the game.
    """
    game = Game()
    game.play()

if __name__ == "__main__":
    main()