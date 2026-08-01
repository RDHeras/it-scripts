import random
import time

# Player stats and setup
class Hero:
    def __init__(self, name, class_choice):
        self.name = name
        self.inventory = ["Health Potion", "Mana Elixir"]
        
        if class_choice == "1":
            self.role = "Archmage"
            self.hp = 70
            self.max_hp = 70
            self.mp = 150
            self.max_mp = 150
            self.attack = 12
            self.spells = {"Fireball": {"cost": 30, "damage": 45}, "Ice Nova": {"cost": 20, "damage": 30}}
        elif class_choice == "2":
            self.role = "Paladin"
            self.hp = 130
            self.max_hp = 130
            self.mp = 60
            self.max_mp = 60
            self.attack = 22
            self.spells = {"Holy Light": {"cost": 25, "heal": 40}, "Smite": {"cost": 20, "damage": 35}}
        else:
