import sys
import os
import random
import pickle
import math
import time


# --Version 0.0.7 --
# Kah Shin

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

    def newPlayer(self):
        print("Hello what is your name?")
        nameInput = input("> ")
        if len(nameInput) <= 0:
            print("Please input something.")
            self.newPlayer()
        else:
            self.name = nameInput

    def profile(self):
        profile = f"\n\n=====Profile=====\n\nName: {self.name}\nAttack: {self.attack}\nCurrent Weapon: {self.curweap}\nClass: {self.Class}\nHealth: {self.health}/{self.maxhealth}\nMana: {self.mana}/{self.maxmana}\nGold: {self.gold}\nLevel: {self.lvl}\nExp: {self.xp}/{self.lvlNext}"
        return profile

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


class gamePlay:
    def __init__(self, state, progress):
        self.state = state
        self.progress = progress
        self.monsters = {
            "Skeleton": Monster('Skeleton', "80", "10", "2", "15", "5", "0"),
            "Goblin": Monster('Goblin', "50", "15", "3", "15", "5", "0")
        }
        self.hero = Player("Default")

    def newPlayer(self):
        self.hero.newPlayer()
        self.main()

    def lobby(self):
        # Displays the Stats of the Player
        print(self.hero.profile())
        decision = input(
            "1. Enter The Dungeon\n"
            "2. Store\n"
            "3. Inventory\n"
            "4. Tavern\n"
            "5. Quit\n"
            "> "
        )

        if decision == '1':
            self.fightSystem(self.experiencePoints)
        if decision == '2':
            pass
        if decision == '3':
            pass
        if decision == '4':
            pass
        if decision == '5':
            self.state = False
        else:
            pass
    
    def experiencePoints(self):
        if self.hero.xp >= self.hero.lvlNext:
            self.hero.lvl += 1
            self.hero.maxhealth += 20
            self.hero.health = self.hero.maxhealth
            self.hero.maxmana += 5
            self.hero.mana = self.hero.maxmana
            self.hero.base_attack += 5
            self.hero.xp = self.hero.xp - self.hero.lvlNext
            self.hero.lvlNext = self.hero.lvlNext*1.5
            print("You have leveled up to Level %i" % self.hero.lvl)
            input(' ')
            if self.hero.lvl == 3:
                # p_class()
                pass
            if self.hero.lvl % 5 == 0:
                # learn()
                pass
        else:
            pass

    def combat(self):
        while (int(self.hero.health) > 0 and int(self.monsters['Goblin'].health) > 0):
            if (self.monsters['Goblin'].speed > self.hero.speed):
                e_dmg = random.randint(round((int(self.monsters['Goblin'].attack) * .7)), round((int(self.monsters['Goblin'].attack) * 1.3)))
                print(f"{self.monsters['Goblin'].name} hit {self.hero.name} for {e_dmg} Damage.")
                self.hero.health -= int(e_dmg)
            else:
                p_dmg = random.randint(round(int(self.hero.attack) * 0.7), round((int(self.hero.attack) * 1.3)))
                print(f"{self.hero.name} hit {self.monsters['Goblin'].name} for {p_dmg} Damage.")
                self.monsters['Goblin'].health = int(self.monsters['Goblin'].health) - p_dmg

        if self.hero.health <= 0:
            return "lost"
        elif self.monsters['Goblin'].health <= 0:
            return "win"

    def fightSystem(self, _callback = None):
        print(f"{self.hero.name} {self.hero.health}/{self.hero.maxhealth}health \n vs \n{self.monsters['Goblin'].name} ??/??health")
        print("1.Attack")
        print("2.Skills")
        print("3.Ultimato")
        print("4.Escape")
        choice = input("What would you do?\n> ")

        if choice == '1':
            result = self.combat()
        elif choice == '2':
            # skills()
            pass
        elif choice == '3':
            # ultimato()
            pass
        elif choice == "4":
            # escape()
            pass

        self.post_fight(result)

        if _callback:
            _callback()

    def post_fight(self, result):
        if result == "win":
            self.monsters['Goblin'].health = self.monsters['Goblin'].maxhealth
            self.monsters['Goblin'].dcount += 1
            self.hero.gold += self.monsters['Goblin'].gold
            self.hero.xp += self.monsters['Goblin'].exp
            print("You have Successfully defeated %s!" % self.monsters['Goblin'].name)
            print("You have found %i gold " % self.monsters['Goblin'].gold)
            # uplvl()
            input("Press any key to continue")
        else:
            self.hero.health = self.hero.maxhealth
            self.hero.mana = self.hero.maxmana
            self.monsters['Goblin'].health = self.monsters['Goblin'].maxhealth
            print("You have been Defeated!")
            input("Press any key to revive")

    def main(self, _callback=None):
        self.lobby()


gameplay = gamePlay(True, 0)
gameplay.newPlayer()
while (gameplay.state == True):
    gameplay.main()
