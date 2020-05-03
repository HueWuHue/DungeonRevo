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
Version: 0.0.4
Added Attack Feature
-Mcost
-Bonus atk from spd
Added Tavern Feature
-Questlog
-Gossip
'''

# Home Page to navigate around everywhere
def start():
    uplvl()
    # Displays the Stats of the Player
    print(
        f"Name: {PlayerIG.name}\nAttack: {PlayerIG.attack}\nCurrent Weapon: {PlayerIG.curweap}\nHealth: {PlayerIG.health}/{PlayerIG.maxhealth}\nMana: {PlayerIG.mana}/{PlayerIG.maxmana}\nGold: {PlayerIG.gold}\nLevel: {PlayerIG.lvl}\nExp: {PlayerIG.xp}"
    )
    decision = input("1. Enter The Dungeon\n2. Store\n3. Inventory\n4. Tavern\n5. Save and load\n> ")

    if decision == '1':
        fight()
    if decision == '2':
        store()
    if decision == '3':
        inventory()
    if decision == '4':
        tavern()
    if decision == '5':
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
        self.mcost = 10
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
            attack += 100
        if self.curweap == "Knive":
            attack += 100

        return attack
    def mcost(self):
        mcost = self.mcost
        if self.curweap == 'Rusty Sword':
            mcost += 5
        if self.curweap == 'Sword':
            mcost += 15
        if self.curweap == 'Axe':
            mcost += 20
        if self.curweap == "Pickaxe":
            mcost += 50
        if self.curweap == "Knive":
            mcost += 20
        return mcost
class Monster:
    def __init__(self, name, maxhealth , attack, speed, gold, exp, dcount):
        self.name = name
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.attack = attack
        self.speed = int(speed)
        self.gold = int(gold)
        self.exp = int(exp)
        self.dcount = int(dcount)
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
skeleton = Monster('Skeleton', "80", "10", "2", "15", "5","0")
grpMonster.append(skeleton)
goblin = Monster('Goblin', "50", "15", "3", "15", "5","0")
grpMonster.append(goblin)
class Questlog:
    def __init__(self, name, reqnum,reward):
        self.name = name
        self.reqnum = reqnum
        self.reward = reward
grpQuest = []
gobslyer = Questlog('Goblin slayer',20,300)
grpQuest.append(gobslyer)
skeslyer = Questlog('Rotting bones',20,300)
grpQuest.append(skeslyer)

class Weapon:
    def __init__(self, name, cost, dmg, mcost):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.mcost = mcost
grpWeapon = []
knive = Weapon('Knive',5000,500,20)
grpWeapon.append(knive)
pickaxe = Weapon('Pickaxe',3000,150,30)
grpWeapon.append(pickaxe)
axe = Weapon('Axe',1000,100,30)
grpWeapon.append(axe)
sword = Weapon('Sword',500,30,15)
grpWeapon.append(sword)

class Pots:
    def __init__(self, name, cost, hpregen, mregen, atkboost, hpboost, spdboost):
        self.name = name
        self.cost = cost
        self.hpregen = hpregen
        self.mregen = mregen
        self.atkboost = atkboost
        self.hpboost = hpboost
        self.spdboost = spdboost


Items = {"Potions": 20,
         "Super Potions": 50
         }


# Fight System **Work in Progress(Maybe TurnBased Is btr?)**
enemy = random.choice(grpMonster)
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
        fight()
    if choice == '3':
        print("YOU CAN'T RUN FROM THE DUNGEON")
        fight()
def attack():
    os.system('cls')
    while (PlayerIG.health) > 0 or (enemy.health) > 0:
            if (PlayerIG.speed) > int(enemy.speed):
                Pturn()
                Eturn()
                while PlayerIG.speed > int(enemy.speed)*2:

                    PlayerIG.speed -= enemy.speed
            else:
                Eturn()
                Pturn()

def Pturn():
    PlayerIG.mana -= PlayerIG.mcost
    if PlayerIG.mana > 0:
        p_attack = random.randint(round((int(PlayerIG.attack) * 0.7)), round((int(PlayerIG.attack) * 1.3)))
        print(f"{PlayerIG.name} hit {enemy.name} for {p_attack} Damage.")
        enemy.health = int(enemy.health) - (p_attack)
        print(f"{PlayerIG.name} health: {PlayerIG.health}\n{enemy.name} health: {enemy.health}\n")
    else:rest()
    if (PlayerIG.health) <= 0:
        die()
    if (enemy.health) <= 0:
        win()
def PAturn():
    PlayerIG.mana -= PlayerIG.mcost/2
    if PlayerIG.mana > 0:
        p_attack = random.randint(round((int(PlayerIG.attack) * 0.7)), round((int(PlayerIG.attack) * 1.3)))
        print(f"{PlayerIG.name} hit {enemy.name} for {p_attack} Damage.")
        enemy.health = int(enemy.health) - (p_attack)
        print(f"{PlayerIG.name} health: {PlayerIG.health}\n{enemy.name} health: {enemy.health}\n")
    else:rest()
    if (PlayerIG.health) <= 0:
        die()
    if (enemy.health) <= 0:
        win()

def Eturn():
    e_attack = random.randint(round((int(enemy.attack) * .7)), round((int(enemy.attack) * 1.3)))
    print(f"{enemy.name} hit {PlayerIG.name} for {e_attack} Damage.")
    (PlayerIG.health) -= int(e_attack)
    print(f"{PlayerIG.name} health: {PlayerIG.health}\n{enemy.name} health: {enemy.health}\n")
    if (PlayerIG.health) <= 0:
        die()
    if (enemy.health) <= 0:
        win()
def rest():
    PlayerIG.mana += PlayerIG.maxmana*0.2
    restamount = PlayerIG.maxmana*0.2
    print("You've recovered",restamount,"mana.")

def die():#perhaps add some loses after u die
    os.system('cls')
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.mana = PlayerIG.maxmana
    enemy.health = enemy.maxhealth
    print("You have been Defeated!")
    option = input("Press any key to revive")
    start()

def win():
    os.system('cls')
    enemy.health = enemy.maxhealth
    enemy.dcount += 1
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
        PlayerIG.maxmana += 5
        PlayerIG.mana =PlayerIG.maxmana
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

    elif option == 'b':
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
    print(f"Hello {PlayerIG.name}! Welcome to Ornn Hub!.\nYou currently have {PlayerIG.gold} Gold.\nPress b to back")
    print("")
    # Shows a list of weapons available
    num = 1
    for weapon in grpWeapon:
        print(num, ". ", weapon.name, ":", str(weapon.cost)+" Gold" ,str(weapon.dmg)+"Attack",str(weapon.mcost)+"Mcost")
        num += 1
    print("\n")
    option = (input("What would you like to buy today?\nWe are never out of stock!\n> "))
    if option.isalpha():
        start()
    if option.isnumeric():
        choice = int(option) - 1
        purchase = grpWeapon[choice]
        print(f'Are you sure you want to buy {grpWeapon[choice].name}?')

        choice = input("> ")
        if choice == "y" or "yes":
            if PlayerIG.gold >= purchase.cost:
                PlayerIG.gold -= purchase.cost
                PlayerIG.weapon.append(purchase.name)
                print(f"You have successfully purchased {purchase.name}.")
                option = input("")
                store()
            else:
                print("You have not enough gold.")
                store()
        else:
            store()
    else:
        print("Please input a valid number.")
        store()
#TavernPageForFoodNDrinks
def tavern():
    print(f"Hello!Welcome to Bob's Tavern.")
    print("")
    print("1. Have a seat\n2. Check out the Quest Log\nPress b to back")
    #showsFoodNdrink
    option = input("What would you like to do?\n>")
    if option.isalpha():
        start()
    if option == '1':
        gossip()
    if option == '2':
        quest()
Gossip = ("I heard TaurusSteak increase your strength","Magic does more damage but uses a lot of Mana","After level 10,you can pick a class to go to","Pegasus are so fast due to their wings")
Race = ("Human","Elf","Dwarf","Demon")
Class = ("Rogue","Warrior","Mage","Assasin","Standholder")
def gossip():
    print("You sat down in the tavern,looking around aimlessly\nSuddenly,you overheard a conversation from a", random.choice(Race) , random.choice(Class))
    print(random.choice(Gossip))
    input("Press b to go back\n>")
def quest():
    if goblin.dcount > gobslyer.reqnum:
        PlayerIG.gold += gobslyer.reward
        goblin.dcount -= gobslyer.reqnum
        print("You've comepleted the quest!Here's your reward!")
        print("You currently have",PlayerIG.gold)
    else:
        print("You have slained ",goblin.dcount,goblin.name,".",(gobslyer.reqnum-goblin.dcount),"more to claim your reward!")
    if skeleton.dcount > skeslyer.reqnum:
        PlayerIG.gold += skeslyer.reward
        skeleton.dcount -= skeslyer.reqnum
        print("You've completed the quest!Here's your reward!")
        print("You currently have",PlayerIG.gold)
    else:
        print("You have slained ",skeleton.dcount,skeleton.name,".",(skeslyer.reqnum-skeleton.dcount),"more to claim your reward!")
    input("Press b to go back\n>")


main()
