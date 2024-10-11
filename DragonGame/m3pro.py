# -*- coding: utf-8 -*-

"""
This program allows a user to play a fun game, runs on python OOP
m3pro game
10/8/2024
Amy Santjer

"""


from m3pro_class import Character, Player, Enemy, Goblin, Orc, Dragon

class Room:
    """Represents a room in the dungeon."""
    def __init__(self, description):
        self.__description = description
        self.__enemy = None
        self.__item = None

    def add_enemy(self, enemy):
        """Adds an enemy to the room."""
        self.__enemy = enemy

    def add_item(self, item):
        """Adds an item to the room."""
        self.__item = item

    def get_description(self):
        """Returns the room description."""
        return self.__description

    def get_enemy(self):
        """Returns the enemy in the room."""
        return self.__enemy

    def get_item(self):
        """Returns the item in the room."""
        return self.__item

    def remove_item(self):
        """Removes the item from the room."""
        self.__item = None

class Game:
    """Manages the game flow and interactions."""
    def __init__(self):
        self.__player = None
        self.__rooms = []
        self.__current_room = 0

    def create_player(self, name):
        """Creates a new player character."""
        self.__player = Player(name)

    def create_rooms(self):
        """Initializes the dungeon rooms."""
        room_descriptions = [
            "A dark cave entrance",
            "A dimly lit corridor",
            "A grand hall with ancient pillars",
            "A small treasure room",
            "The lair of the final boss"
        ]
        for desc in room_descriptions:
            self.__rooms.append(Room(desc))

        # Add enemies and items to rooms
        self.__rooms[1].add_enemy(Goblin())
        self.__rooms[2].add_enemy(Orc())
        self.__rooms[3].add_item("Health Potion")
        self.__rooms[4].add_enemy(Dragon())

    def play(self):
        """Main game loop."""
        print("Welcome to the Delicious in Dungeon Game!")
        player_name = input("Enter your character's name: ")
        self.create_player(player_name)
        self.create_rooms()

        while self.__player.is_alive() and self.__current_room < len(self.__rooms):
            self.process_room()

        if self.__player.is_alive():
            print("\nCongratulations! You've completed the dungeon!")
        else:
            print("\nGame Over. Your character has been defeated! :c")

    def process_room(self):
        """Handles events in the current room."""
        room = self.__rooms[self.__current_room]
        print(f"\n{room.get_description()}")

        enemy = room.get_enemy()
        if enemy:
            self.combat(enemy)
        
        item = room.get_item()
        if item:
            print(f"\nYou found a {item}!")
            self.__player.add_to_inventory(item)
            room.remove_item()

        if self.__player.is_alive():
            self.player_action()

    def combat(self, enemy):
        """Manages combat between player and enemy."""
        print(f"A {enemy.get_name()} appears!")
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
            loot = enemy.drop_loot()
            if loot:
                print(f"The {enemy.get_name()} dropped: {loot}")
                self.__player.add_to_inventory(loot)
            self.__player.gain_exp(enemy.get_exp_reward())

    def player_action(self):
        """Handles player actions between rooms."""
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
                print("Invalid action. Please try again.")

    def use_item(self):
        """Allows the player to use an item from their inventory."""
        if not self.__player.get_inventory():
            print("\nOh no! Your inventory is empty! Move into more dungeons or defeat monsters to get items!")
            return

        print("\nYour inventory:", self.__player.get_inventory())
        item = input("Which item would you like to use? ")
        try:
            self.__player.use_item(item)
        except ValueError as e:
            print(str(e))

def main():
    """Entry point of the game."""
    game = Game()
    game.play()

if __name__ == "__main__":
    main()