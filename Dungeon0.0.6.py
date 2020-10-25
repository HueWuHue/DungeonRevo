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
---Version: 0.0.5---
Fixed same enemy problem
---Version: 0.0.6---
Fight system resolved,now its turn based
able to learn and use skill
---Problem to be solved---
skill dmg is not rounded
fight system options3 and 4 unusable
-----------------
Tavern quite useless
Addition of Pet system?
Main quest log?
Plot?
Partners or Teammates?
Class system?
Class Weapons?
Forge system?
Material drop form monster?
Monster Design?
Monster Dictionary?
Armor and MR?
Mana?
                    .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$ 
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$      Why Do I Hear BOSS Music?
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            """""                              "$$$"
'''


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.maxmana = 100
        self.mana = self.maxmana
        self.base_attack = 100
        self.mcost = 0
        self.gold = 0
        self.pot = 2
        self.weapon = []
        self.curweap = []
        self.speed = 5
        self.lvl = 4
        self.xp = 0
        self.lvlNext = 5
        self.Class = "Warrior"

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


class Monster:
    def __init__(self, name, maxhealth, m_attack, speed, gold, exp, dcount):
        self.name = name
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.attack = m_attack
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
skeleton = Monster('Skeleton', "80", "10", "2", "15", "5", "0")
grpMonster.append(skeleton)
goblin = Monster('Goblin', "50", "15", "3", "15", "5", "0")
grpMonster.append(goblin)


def p_class():
    print("You have reached Level 3!It's time to pick a class to go with")
    print("1.Warrior\n"
          "2.Mage\b"
          "3.Rogue\n"
          )
    option = int(input('>'))
    if option == 1:
        PlayerIG.Class = "Warrior"
    if option == 2:
        PlayerIG.Class = "Mage"
    if option == 3:
        PlayerIG.Class = "Rogue"


def learn():
    i = 0
    if PlayerIG.Class == "Warrior":
        skillslot.append(WarriorST[i])
        print(f"Congratulation,you've learned how to cast {WarriorST[i].name}!")
    if PlayerIG.Class == "Mage":
        skillslot.append(MageST[MageSTname[int(PlayerIG.lvl / 5 - 1)]])
        print(f"Congratulation,you've learned how to cast {MageSTname[int(PlayerIG.lvl / 5 - 1)]}")
    if PlayerIG.Class == "Rogue":
        skillslot.append(RogueST[RogueSTname[int(PlayerIG.lvl / 5 - 1)]])
        print(f"Congratulation,you've learned how to cast {RogueST[RogueSTname[int(PlayerIG.lvl / 5 - 1)]]}")


class Skill:
    def __init__(self, name, mcost, power, cooldown):
        self.name = name
        self.mcost = mcost
        self.power = power
        self.cooldown = cooldown
        self.stats = [
            self.name,
            self.mcost,
            self.power,
            self.cooldown
        ]


skillslot = []
# =====SkillTrees=====
WarriorST = []
slash = Skill("Slash", 10, 1.2, 2)
WarriorST.append(slash)
bladestorm = Skill("BladeStorm", 40, 2, 3)
WarriorST.append(bladestorm)
demacia = Skill("DEMACIA!", 100, 10, 11)
WarriorST.append(demacia)
MageST = {"Fireball": [Skill("Fireball", 20, 1.5, 1)],
          "Ice shard": [Skill("Ice shard", 10, 1.2, 1)],
          "Pyroblast": [Skill("Pyroblast", 100, 12, 21)]}
MageSTname = ["Fireball", "Ice shard", "Pyroblast"]
RogueST = {"Backstab": [Skill("Backstab", 15, 1.1, 1)],
           "Sinister Strike": [Skill("Sinister Strike", 20, 1.5, 2)],
           "Crimson Tempest": [Skill("Crimson Tempest", 50, 5, 5)]}
RogueSTname = ["Backstab", "Sinister Strike", "Crimson Tempest"]


class Questlog:
    def __init__(self, name, reqnum, reward):
        self.name = name
        self.reqnum = reqnum
        self.reward = reward


grpQuest = []
gobslyer = Questlog('Goblin slayer', 20, 300)
grpQuest.append(gobslyer)
skeslyer = Questlog('Rotting bones', 20, 300)
grpQuest.append(skeslyer)


class Weapon:
    def __init__(self, name, cost, dmg, mcost):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.mcost = mcost


grpWeapon = []
knive = Weapon('Knive', 5000, 500, 20)
grpWeapon.append(knive)
pickaxe = Weapon('Pickaxe', 3000, 150, 30)
grpWeapon.append(pickaxe)
axe = Weapon('Axe', 1000, 100, 30)
grpWeapon.append(axe)
sword = Weapon('Sword', 500, 30, 15)
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


# Home Page to navigate around everywhere
def start():
    # Displays the Stats of the Player
    print(
        "=====Profile=====\n"
        f"Name: {PlayerIG.name}\n"
        f"Attack: {PlayerIG.attack}\n"
        f"Current Weapon: {PlayerIG.curweap}\n"
        f"Class: {PlayerIG.Class}\n"
        f"Health: {PlayerIG.health}/{PlayerIG.maxhealth}\n"
        f"Mana: {PlayerIG.mana}/{PlayerIG.maxmana}\n"
        f"Gold: {PlayerIG.gold}\n"
        f"Level: {PlayerIG.lvl}\n"
        f"Exp: {PlayerIG.xp}/{PlayerIG.lvlNext}"
    )
    decision = input("1. Enter The Dungeon\n"
                     "2. Store\n"
                     "3. Inventory\n"
                     "4. Tavern\n"
                     "> ")

    if decision == '1':
        fight()
    if decision == '2':
        store()
    if decision == '3':
        inventory()
    if decision == '4':
        tavern()
    else:
        start()


# Fight System **Work in Progress(Just need a little touch up)**
enemy = random.choice(grpMonster)


def fight():
    print(f"{PlayerIG.name} {PlayerIG.health}/{PlayerIG.maxhealth}health \n vs \n{enemy.name} ??/??health")
    print("1.Attack")
    print("2.Skills")
    print("3.Ultimato")
    print("4.Escape")
    choice = input("What would you do?\n> ")

    if choice == '1':
        attack()
    elif choice == '2':
        skills()
    elif choice == '3':
        ultimato()
    elif choice == "4":
        escape()


def attack():

    if enemy.speed > PlayerIG.speed:
        e_turn()
        p_turn()
        fight()
    else:
        p_turn()
        e_turn()
        fight()


def p_turn():
    p_dmg = random.randint(round(int(PlayerIG.attack) * 0.7), round((int(PlayerIG.attack) * 1.3)))
    print(f"{PlayerIG.name} hit {enemy.name} for {p_dmg} Damage.")
    enemy.health = int(enemy.health) - p_dmg
    fight_over()


def e_turn():
    e_dmg = random.randint(round((int(enemy.attack) * .7)), round((int(enemy.attack) * 1.3)))
    print(f"{enemy.name} hit {PlayerIG.name} for {e_dmg} Damage.")
    PlayerIG.health -= int(e_dmg)
    fight_over()


def skills():
    print("Skill list")
    usable = 0
    for i in range(len(skillslot)):
        print(f"{i+1}.{skillslot[i].name} Mocst:{skillslot[i].mcost} Power:{skillslot[i].power} Cooldown:{skillslot[i].cooldown}\n")
        usable += 1
    option = int(input(""))
    if option > usable:
        print("Not a valid option")
        skills()
    else:
        p_dmg = random.randint(round(int(PlayerIG.attack) * 0.7), round((int(PlayerIG.attack) * 1.3)))
        p_dmg *= skillslot[option-1].power
        print(f"{PlayerIG.name} hit {enemy.name} for {p_dmg} Damage.")
        enemy.health = int(enemy.health) - p_dmg
        fight_over()


def fight_over():
    if enemy.health <= 0:
        win()
    elif PlayerIG.health <= 0:
        die()


def die():
    # perhaps add some loses after u die
    global enemy
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.mana = PlayerIG.maxmana
    enemy.health = enemy.maxhealth
    print("You have been Defeated!")
    input("Press any key to revive")
    enemy = random.choice(grpMonster)
    start()


def win():
    global enemy
    enemy.health = enemy.maxhealth
    enemy.dcount += 1
    PlayerIG.gold += enemy.gold
    PlayerIG.xp += enemy.exp
    print("You have Successfully defeated %s!" % enemy.name)
    print("You have found %i gold " % enemy.gold)
    uplvl()
    input("Press any key to continue")
    enemy = random.choice(grpMonster)

    start()


def start1():
    pass


# First page when player starts the game
def main():

    print("Hello what is your name?")
    option1 = input("> ")
    global PlayerIG
    if len(option1) <= 0:

        print("Please input something.")
        start()
    else:
        PlayerIG = Player(option1)
        start()


# =====Leveling system for the game=====
def uplvl():
    if PlayerIG.xp >= PlayerIG.lvlNext:
        PlayerIG.lvl += 1
        PlayerIG.maxhealth += 20
        PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.maxmana += 5
        PlayerIG.mana = PlayerIG.maxmana
        PlayerIG.base_attack += 5
        PlayerIG.xp = PlayerIG.xp - PlayerIG.lvlNext
        PlayerIG.lvlNext = PlayerIG.lvlNext*1.5
        print("You have leveled up to Level %i" % PlayerIG.lvl)
        input(' ')
        if PlayerIG.lvl == 3:
            p_class()
        if PlayerIG.lvl % 5 == 0:
            learn()
    else:
        pass


def inventory():

    print("What would you like to do?")
    print("\n1. Equip Weapons")
    print("2. Drink Potions")
    print("\nBack")
    option = input("> ")

    if option == '1':
        equip()

    elif option == '2':

        if PlayerIG.pot == 0:
            print("You don't have any potions left")
        else:
            PlayerIG.health += 20
            if PlayerIG.health > PlayerIG.maxhealth:
                PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.pot -= 1
            print("You drank a potion")
        input(' ')
        inventory()

    elif option == 'b':
        start1()

    else:
        inventory()

# =====ChangeWeapon=====


def equip():

    print("You are currently equipped with %s." % PlayerIG.curweap)
    print("What do you want to equip?\n")
    for weapon in PlayerIG.weapon:
        print(weapon)
    print("Enter b to go back.")
    option = input("> ")
    if option == PlayerIG.curweap:
        print("You have already equipped that item")
        input(' ')
        equip()
    elif option == 'b':
        inventory()
    elif option in PlayerIG.weapon:
        PlayerIG.curweap = option
        print("You have equipped %s." % option)
        input(' ')
        equip()
    else:
        print("You do not own %s." % option)


# =====StorePageForWeapnNPots=====
def store():
    print(f"Hello {PlayerIG.name}! Welcome to Ornn Hub!.\nYou currently have {PlayerIG.gold} Gold.\nPress b to back")
    print("")
    # Shows a list of weapons available
    num = 1
    for weapon in grpWeapon:
        print(num, ". ", weapon.name, ":", str(weapon.cost)+" Gold", str(weapon.dmg)+"Attack", str(weapon.mcost)+"Mcost")
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
                input("")
                store()
            else:
                print("You have not enough gold.")
                store()
        else:
            store()
    else:
        print("Please input a valid number.")
        store()


# =====TavernPageForQuest=====
def tavern():
    print(f"Hello!Welcome to Bob's Tavern.")
    print("")
    print("1. Have a seat\n2. Check out the Quest Log\nPress b to back")
    # showsFoodNdrink
    option = input("What would you like to do?\n>")
    if option.isalpha():
        start()
    if option == '1':
        gossip()
    if option == '2':
        quest()


Gossip = ("I heard TaurusSteak increase your strength",
          "Magic does more damage but uses a lot of Mana",
          "After level 3,you can pick a class to go to.",
          "Pegasus are so fast due to their wings,if only I had wings man.",
          "The Dev is still working hard for this.")
gossipRace = ("Human", "Elf", "Dwarf", "Demon")
gossipClass = ("Rogue", "Warrior", "Mage", "Assasin", "Standholder")


def gossip():
    print("You sat down in the tavern,looking around aimlessly\nSuddenly,you overheard a conversation from a", random.choice(gossipRace), random.choice(gossipClass))
    print(random.choice(Gossip))
    input("Press b to go back\n>")


def quest():
    if goblin.dcount > gobslyer.reqnum:
        PlayerIG.gold += gobslyer.reward
        goblin.dcount -= gobslyer.reqnum
        print("You've completed the quest!Here's your reward!")
        print("You currently have", PlayerIG.gold)
    else:
        print("You have slained ", goblin.dcount, goblin.name, ".", (gobslyer.reqnum-goblin.dcount), "more to claim your reward!")
    if skeleton.dcount > skeslyer.reqnum:
        PlayerIG.gold += skeslyer.reward
        skeleton.dcount -= skeslyer.reqnum
        print("You've completed the quest!Here's your reward!")
        print("You currently have", PlayerIG.gold)
    else:
        print("You have slain ", skeleton.dcount, skeleton.name, ".", (skeslyer.reqnum-skeleton.dcount), "more to claim your reward!")
    input("Press b to go back\n>")


main()
