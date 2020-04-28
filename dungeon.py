import sys
import os
import random
import pickle
import math
import time

'''
Version: 0.0.2
'''

Weapons = {'Sword': 40,
           'Dagger': 30,
           'Axe': 100,
           'Pickaxe': 150,
           'Knive': 350,
           'Club': 50,
           }

Items = {"Potions": 30
         }

Magic = {"Fireball",
         "Ice Shards",
         "Ghoul"}


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 25
        self.gold = 0
        self.pot = 2
        self.weapon = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]
        self.lvl = 1
        self.xp = 0
    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == 'Rusty Sword':
            attack += 5

        if self.curweap == 'Sword':
            attack += 15

        if self.curweap == 'Axe':
            attack += 20

        if self.curweap == "Pickaxe":
            attack += 40

        if self.curweap == "Knive":
            attack += 100
        return attack

class Monster:
    def __init__(self, name, class_, attack, gold, exp):
        self.name = name
        self.class_ = class_
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = attack
        self.gold = int(gold)
        self.exp = int(exp)
        # Use the stats property to view all the stats of the Character
        self.stats = [
            self.name,
            self.class_,
            self.maxhealth,
            self.attack,
            self.gold,
            self.exp,
        ]


class Weapon:
    def __init__(self, name, cost, dmg, mcost):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.mcost = mcost

# Enemy Names(add new monster names here)
Beast_names = [
    'Goblin',
    'Skeletons',
    'Dragon',
    'Golem',
    'Wolf'
]

Attr = [
    "Fire",
    "Earth",
    "Magic",
    "Warrior",
]

goblin = Monster(Beast_names[0], Attr[3], "30", "50", "5")


# Fight System **Work in Progress**


def fight():
    global Monster
    global PlayerIG
    Rusty_Sword = Weapon("Rusty_Sword", 50, 5, 10)
    print(f"{PlayerIG.name} vs {goblin.name}")
    choice = input("What would you do?\n> ")
    p_attack = random.randint(round((int(PlayerIG.base_attack) * 0.7)), round((int(PlayerIG.base_attack) * 1.3)))

    if choice == '1':
        while PlayerIG.health > 0 or goblin.health > 0:
            turn = random.choice(("P", "E"))
            if turn == "P":
                if len(PlayerIG.curweap) > 0:
                    for i in PlayerIG.curweap:
                        i = Weapon(f"{i}", 50, 5, 10)
                    p_attack += i.dmg
                print(f"{PlayerIG.name} hit {goblin.name} for {p_attack} Damage.")
                goblin.health -= p_attack
                print(
                    f"{PlayerIG.name} health: {PlayerIG.health}\n{goblin.name} health: {goblin.health}\n")
            else:
                e_attack = random.randint(round((int(goblin.attack) * .7)), round((int(goblin.attack) * 1.3)))

                print(f"{goblin.name} hit {PlayerIG.name} for {e_attack} Damage.")
                PlayerIG.health -= e_attack
                print(
                    f"{PlayerIG.name} health: {PlayerIG.health}\n{goblin.name} health: {goblin.health}\n")
            if PlayerIG.health <= 0:
                die()
            if goblin.health <= 0:
                 win()
def die():
    os.system('cls')
    PlayerIG.health = PlayerIG.maxhealth
    goblin.health = goblin.maxhealth
    print("You have been Defeated!")
    start()

def win():
    os.system('cls')
    goblin.health = goblin.maxhealth
    PlayerIG.gold += goblin.gold
    PlayerIG.xp += goblin.exp
    uplvl()
    option = input(' ')
    print("You have Successfully defeated %s!" % goblin.name)
    print("You have found %i gold " % goblin.gold)
    start()

def start1():
    pass

# First page when player starts the game
def main():
    os.system('cls')
    print("Hello what is your name?")
    option1 = input("> ")
    global PlayerIG
    if len(option1) <= 0:
        os.system('cls')
        print("Please input something.")
        start()
    else:
        PlayerIG = Player(option1)
        start()


# Leveling system for the game
def uplvl():
    lvlNext = 25
    if PlayerIG.xp >= lvlNext:
        PlayerIG.lvl += 1
        PlayerIG.maxhealth += 25
        PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.base_attack += 10
        PlayerIG.xp = PlayerIG.xp - lvlNext
        lvlNext = round(lvlNext * 1.5)
        print("You have leveled up to Level %i" % PlayerIG.lvl)
        option = input(' ')
        os.system('cls')
    else:
        pass


def store():
    print(f"Hello {PlayerIG.name}! Welcome to Gary's  .\nYou currently have {PlayerIG.gold} Gold.")
    print("**********")
    # Shows a list of weapons available
    for weapon in Weapons:
        print(weapon + ":", str(Weapons[weapon])+" Gold")
    print("**********\n")
    option = input("What would you like to buy today?\n> ")

    if option in Weapons:
        if PlayerIG.gold >= Weapons[option]:
            PlayerIG.gold -= Weapons[option]
            print(f"You have successfully bought {option}!\nYou have {PlayerIG.gold} Gold remaining.")
            time.sleep(1)
        else:
            required = Weapons[option] - PlayerIG.gold
            print(f"You are short of {required} Gold!")
            time.sleep(1)
            store()
    else:
        print(f"{option} does not exist!")
        time.sleep(1)
        store()



# Home Page to navigate around everywhere
def start():
    uplvl()
    # Displays the Stats of the Player
    print(
        f"Name: {PlayerIG.name}\nAttack: {PlayerIG.attack}\nCurrent Weapon: {PlayerIG.curweap}\nHealth: {PlayerIG.health}/{PlayerIG.maxhealth}\nGold: {PlayerIG.gold}\nLevel: {PlayerIG.lvl}\nExp: {PlayerIG.xp}"
    )
    decision = input("1. Fight\n2. Store\n3. Save and Quit\n> ")

    if decision == '1':
        fight()
    if decision == '2':
        store()
    if decision == '3':
        save()
    else:
        start()

main()
