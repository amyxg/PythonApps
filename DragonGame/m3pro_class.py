# -*- coding: utf-8 -*-
"""
This program allows a user to play a fun game, runs on python OOP
m3pro game
10/8/2024
Amy Santjer

"""

import random

class Character:
    """Base class for all characters in the game."""
    
    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    def attack(self):
        """Perform an attack."""
        return self.__attack_power

    def take_damage(self, damage):
        """Receive damage and update health."""
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def is_alive(self):
        """Check if the character is alive."""
        return self.__health > 0

    def display_stats(self):
        """Display the character's current stats."""
        print(f"{self.__name} - Health: {self.__health}, Attack Power: {self.__attack_power}")

    def get_name(self):
        """Returns the character's name."""
        return self.__name

class Player(Character):
    """Represents the player character."""
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=10)
        self.__level = 1
        self.__exp = 0
        self.__inventory = []

    def gain_exp(self, exp):
        """Gain experience and level up if enough exp is accumulated."""
        self.__exp += exp
        if self.__exp >= 100:
            self.level_up()

    def level_up(self):
        """Increase the player's level and stats."""
        self.__level += 1
        self._Character__health += 20
        self._Character__attack_power += 5
        self.__exp = 0
        print(f"{self._Character__name} leveled up to level {self.__level}!")

    def add_to_inventory(self, item):
        """Add an item to the player's inventory."""
        self.__inventory.append(item)

    def use_item(self, item):
        """Use an item from the player's inventory."""
        if item in self.__inventory:
            if item == "Health Potion":
                self._Character__health += 30
                if self._Character__health > 100:
                    self._Character__health = 100
                print(f"{self._Character__name} used a Health Potion and recovered 30 HP.")
            self.__inventory.remove(item)
        else:
            raise ValueError("Item not in inventory")

    def display_stats(self):
        """Display the player's current stats."""
        super().display_stats()
        print(f"Level: {self.__level}, EXP: {self.__exp}")

    def get_inventory(self):
        """Returns the player's inventory."""
        return self.__inventory

class Enemy(Character):
    """Base class for all enemy characters."""
    def __init__(self, name, health, attack_power, exp_reward):
        super().__init__(name, health, attack_power)
        self.__exp_reward = exp_reward

    def drop_loot(self):
        """Drop loot when defeated."""
        return random.choice(["Health Potion", "None"])

    def get_exp_reward(self):
        """Returns the exp reward for defeating this enemy."""
        return self.__exp_reward

class Goblin(Enemy):
    """Represents a Goblin enemy."""
    def __init__(self):
        super().__init__("Goblin", health=30, attack_power=5, exp_reward=20)

class Orc(Enemy):
    """Represents an Orc enemy."""
    def __init__(self):
        super().__init__("Orc", health=50, attack_power=8, exp_reward=40)

class Dragon(Enemy):
    """Represents a Dragon enemy."""
    def __init__(self):
        super().__init__("Dragon", health=100, attack_power=15, exp_reward=100)