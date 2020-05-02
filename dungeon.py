import sys
import os
import random
import pickle
import math
import time
"""this is the area for shit that hvnt got a place

Magic = {"Fireball",
         "Ice Shards",
         "Ghoul"}
"""

'''
Version: 0.0.3
Fight system fixed
Added inventory

'''
#keynotes:Make a better fight system
#Perhaps with any monster other than goblin

# Home Page to navigate around everywhere
def start():
    uplvl()
    # Displays the Stats of the Player
    print(
        f"Name: {PlayerIG.name}\nAttack: {PlayerIG.attack}\nCurrent Weapon: {PlayerIG.curweap}\nHealth: {PlayerIG.health}/{PlayerIG.maxhealth}\nMana: {PlayerIG.mana}/{PlayerIG.maxmana}\nGold: {PlayerIG.gold}\nLevel: {PlayerIG.lvl}\nExp: {PlayerIG.xp}"
    )
    decision = input("1. Enter The Dungeon\n2. Store\n3. Inventory\n4.Save and load\n> ")

    if decision == '1':
        fight()
    if decision == '2':
        store()
    if decision == '3':
        inventory()
    if decision == '4':
        save()
    else:
        start()


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.maxmana = 100
        self.mana = self.maxmana
        self.base_attack = 25
        self.gold = 0
        self.pot = 2
        self.weapon = []
        self.curweap = []
        self.speed = 5
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
    def __init__(self, name, maxhealth , attack, speed, gold, exp):
        self.name = name
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.attack = attack
        self.speed = int(speed)
        self.gold = int(gold)
        self.exp = int(exp)

        # Use the stats property to view all the stats of the Character
        self.stats = [
            self.name,
            self.health,
            self.attack,
            self.speed,
            self.gold,
            self.exp,
        ]

grpMonster = []
goblin = Monster('Goblin', "50", "15", "3", "15", "5")
grpMonster.append(goblin)
skeleton = Monster('Skeleton', "80", "10", "2", "15", "5")
grpMonster.append(skeleton)

class Weapon:
    def __init__(self, name, cost, dmg, mcost):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.mcost = mcost

Weapons = {'Sword': 40,
           'Dagger': 30,
           'Axe': 100,
           'Pickaxe': 150,
           'Knive': 350,
           }

Items = {"Potions": 20,
         "Super Potions": 50
         }


# Fight System **Work in Progress(a lot more to go tbh)**
enemy = random.choice((grpMonster))
def fight():
    global PlayerIG
    print(f"{PlayerIG.name} vs {enemy.name}")
    print("1.Attack")
    print("2.Magic")
    print("3.Run")
    choice = input("What would you do?\n> ")



    if choice == '1':
        attack()
    if choice == '2':
        print("You haven't learnt magic,Muggle")
    if choice == '3':
        print("YOU CAN'T RUN FROM THE DUNGEON")
        fight()
def attack():
    os.system('cls')
    while (PlayerIG.health) > 0 or (enemy.health) > 0:
            if (PlayerIG.speed) > int(enemy.speed):
                p_attack = random.randint(round((int(PlayerIG.attack) * 0.7)), round((int(PlayerIG.attack) * 1.3)))
                print(f"{PlayerIG.name} hit {enemy.name} for {p_attack} Damage.")
                enemy.health = int(enemy.health) - (p_attack)
                print(f"{PlayerIG.name} health: {PlayerIG.health}\n{enemy.name} health: {enemy.health}\n")
                if (PlayerIG.health) <= 0:
                    die()
                if (enemy.health) <= 0:
                    win()
                e_attack = random.randint(round((int(enemy.attack) * .7)), round((int(enemy.attack) * 1.3)))

                print(f"{enemy.name} hit {PlayerIG.name} for {e_attack} Damage.")
                (PlayerIG.health) -= int(e_attack)
                print(f"{PlayerIG.name} health: {PlayerIG.health}\n{enemy.name} health: {enemy.health}\n")
                if (PlayerIG.health) <= 0:
                    die()
                if (enemy.health) <= 0:
                    win()
            else:
                e_attack = random.randint(round((int(enemy.attack) * .7)), round((int(enemy.attack) * 1.3)))

                print(f"{enemy.name} hit {PlayerIG.name} for {e_attack} Damage.")
                (PlayerIG.health) -= int(e_attack)
                print(f"{PlayerIG.name} health: {PlayerIG.health}\n{enemy.name} health: {enemy.health}\n")
                if (PlayerIG.health) <= 0:
                    die()
                if (enemy.health) <= 0:
                    win()
                p_attack = random.randint(round((int(PlayerIG.attack) * 0.7)), round((int(PlayerIG.attack) * 1.3)))
                print(f"{PlayerIG.name} hit {enemy.name} for {p_attack} Damage.")
                enemy.health = int(enemy.health) - (p_attack)
                print(f"{PlayerIG.name} health: {PlayerIG.health}\n{enemy.name} health: {enemy.health}\n")
                if (PlayerIG.health) <= 0:
                    die()
                if (enemy.health) <= 0:
                    win()

def die():#perhaps add some loses after u die
    os.system('cls')
    PlayerIG.health = PlayerIG.maxhealth
    enemy.health = enemy.maxhealth
    print("You have been Defeated!")
    option = input("Press any key to revive")
    start()

def win():#not much else
    os.system('cls')
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.gold
    PlayerIG.xp += enemy.exp
    uplvl()
    print("You have Successfully defeated %s!" % enemy.name)
    print("You have found %i gold " % enemy.gold)
    option = input("Press any key to continue")
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
def inventory():
    os.system('cls')
    print("What would you like to do?")
    print("\n1. Equip Weapons")
    print("2. Drink Potions")
    print("\nBack")
    option = input("> ")

    if option == '1':
        equip()

    elif option == '2':
        os.system('cls')
        if PlayerIG.pot == 0:
            print("You don't have any potions left")
        else:
            PlayerIG.health += 20
            if PlayerIG.health > PlayerIG.maxhealth:
                PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.pot -= 1
            print("You drank a potion")
        option = input(' ')
        inventory()

    elif option == 'back':
        start1()

    else:
        inventory()
#ChangeWeapon
def equip():
    os.system('cls')
    print("You are currently equipped with %s." % PlayerIG.curweap)
    print("What do you want to equip?\n")
    for weapon in PlayerIG.weapon:
        print(weapon)
    print("Enter b to go back.")
    option = input("> ")
    if option == PlayerIG.curweap:
        print("You have already equipped that item")
        option = input(' ')
        equip()
    elif option == 'b':
        inventory()
    elif option in PlayerIG.weapon:
        PlayerIG.curweap = option
        print("You have equipped %s." %option)
        option = input(' ')
        equip()
    else:
        print("You do not own %s." % option)

#StorePageForWeapnNPots
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
            PlayerIG.weapon.append(option)
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





main()
