# -*- coding: utf-8 -*-
"""
This program allows a user to play a fun game, runs on python OOP
m3pro game
10/8/2024
Amy Santjer

"""
import random

class Character:
    """
    Base class for all characters in the game.
    
    """
    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    def attack(self):
        """
        Perform an attack (player and enemy).
        
        returns: attack amount.
        """
        return self.__attack_power

    def take_damage(self, damage):
        """
        Receive damage and update health.
        
        damage: int
        """
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def is_alive(self):
        """
        Check if the character is alive.
        
        returns: health amount.
        """
        return self.__health > 0

    def display_stats(self):
        """
        Display the character's current stats (health and attack power).
        """
        print(f"{self.__name} - Health: {self.__health}, Attack Power: {self.__attack_power}")

    def get_name(self):
        """
        Obtains player's name.

        returns: the character's name.
        """
        return self.__name

class Player(Character):
    """
    Represents the player character.
    
    """
    def __init__(self, name): # name: str
        super().__init__(name, health = 100, attack_power = 10)
        self.__level = 1
        self.__exp = 0
        self.__inventory = []

    def gain_exp(self, exp):
        """
        Gain experience and level up if enough exp is accumulated.

        exp: int
        """
        self.__exp += exp
        print(f"You gained {exp} experience points!")
        if self.__exp >= 100:
            self.level_up()

    def level_up(self):
        """
        Increase the player's level and stats.
        """
        self.__level += 1
        # Using name mangling to access parent class's private attributes
        self._Character__health += 20
        self._Character__attack_power += 5
        self.__exp = 0
        print(f"Level Up! You are now level {self.__level}!")
        print(f"Your health and attack power have increased!")

    def add_to_inventory(self, item):
        """
        Add an item to the player's inventory.

        item: str
        """
        self.__inventory.append(item)
        print(f"Added {item} to inventory.")

    def use_item(self, item):
        """
        Use an item from the player's inventory.

        item: str
        """
        if item in self.__inventory:
            if item == "Health Potion":
                self._Character__health += 30
                if self._Character__health > 100:
                    self._Character__health = 100
                print(f"You used a Health Potion and recovered 30 HP.")
                self.__inventory.remove(item)
            elif item == "Dragon Scale":
                print("The Dragon Scale gleams but doesn't have any immediate effect.")
            else:
                print(f"You can't use {item} right now.")
        else:
            raise ValueError("Item not in inventory")

    def display_stats(self):
        """
        Display the player's current stats.
        """
        super().display_stats()
        print(f"Level: {self.__level}, EXP: {self.__exp}/100")
        if self.__inventory:
            print(f"Inventory: {', '.join(self.__inventory)}")
        else:
            print("Inventory: Empty")

    def get_inventory(self):
        """
        Returns the player's inventory.
        """
        return self.__inventory

class Dragon(Character):
    """
    Base class for all dragon enemies.
    
    """
    def __init__(self, name, health, attack_power, exp_reward):
        super().__init__(name, health, attack_power)
        self.__exp_reward = exp_reward

    def drop_loot(self):
        """
        Drop loot (one item) when enemy is defeated.

        returns: an element from selected list.
        """
        return random.choice(["Health Potion", "Dragon Scale", "None"])

    def get_exp_reward(self):
        """
        Obtains exp points for Player after defeating enemy.

        returns: exp reward for defeating this dragon.
        """
        return self.__exp_reward

class FireDragon(Dragon):
    """
    Represents a Fire Dragon enemy.
    
    """
    def __init__(self):
        super().__init__("Fire Dragon", health = 40, attack_power = 7, exp_reward = 30) # update Dragon's info from parent
    
    def special_ability(self):
        """
        Fire breath attack
        
        returns: string statement
        """
        return "breathes fire"

class IceDragon(Dragon):
    """
    Represents an Ice Dragon enemy.
    """
    def __init__(self):
        super().__init__("Ice Dragon", health = 50, attack_power = 8, exp_reward = 40)
    
    def special_ability(self):
        """
        Frost breath attack
        
        returns: string statement
        """
        return "freezes with frost breath"

class ElderDragon(Dragon):
    """
    Represents an Elder Dragon enemy (final boss).
    
    """
    def __init__(self):
        super().__init__("Elder Dragon", health = 100, attack_power = 15, exp_reward = 100)
    
    def special_ability(self):
        """
        Ancient magic attack
        
        returns: string statement
        """
        return "uses ancient dragon magic"