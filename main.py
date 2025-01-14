import random
import time
from colorama import Fore, Back, Style
from sys import stdout

def tprint(text):
    time.sleep(0.8)
    for c in text:
        print(c,end="")
        stdout.flush()
        time.sleep(0.05)
    print()
    
def tinput(text):
    time.sleep(0.8)
    for c in text:
        print(c,end="")
        stdout.flush()
        time.sleep(0.05)
    inp = input()
    return inp

class Character:
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.intelligence = intelligence
        self.wisdom = wisdom 
        self.cRate = cRate
        self.cDmg = cDmg
        self.penRate = penRate
        self.incMight = incMight
        self.dmgReduction = dmgReduction
        self.manaRegen = manaRegen
        self.accuracy = accuracy
        self.potions = potions
        self.maxHealth = health
        self.mana = 0
        self.ultMana = 120
        self.poisonTurns = 0
        self.contaminated = False

    def takeDamage(self, damage, crit):
        self.mana += 5 * self.manaRegen
        if crit == True:
            if damage < 1:
                self.health -= 1
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + "1" + Style.RESET_ALL + " damage!")
            else:
                self.health -= (damage*(1-self.dmgReduction))
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + str(round(damage*(1-self.dmgReduction), 2)) + Style.RESET_ALL + " damage!")
        else:
            if damage < 1:
                self.health -= 1
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken 1 damage!")
            else:
                self.health -= (damage*(1-self.dmgReduction))
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + str(round(damage*(1-self.dmgReduction), 2)) + " damage!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts a cantrip on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts a cantrip on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts a cantrip on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def potion(self,target):
        originalHealth = self.health
        self.health += 120
        self.mana += 30 * self.manaRegen

        if self.health > self.maxHealth:
            self.health = self.maxHealth
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used a potion and recovered " + str(self.health - originalHealth) + " health!")

        else:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used a potion and recovered 120 health!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
        self.potions -= 1

        if self.contaminated == True:
            self.poisoned(target)
            self.poisonTurns += 1

    def ult(self):
        pass

    def poisoned(self,target):
        self.health -= target.wisdom*2.25
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " took " + Fore.GREEN + str(target.wisdom*1.5) + Style.RESET_ALL + " Poison damage!")
        self.poisonTurns -= 1

class Barbarian(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 100

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Bloody Cleave on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if self.health <= self.maxHealth/2:
                crit -= 30
                if crit > self.cRate:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Bloody Cleave on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 2.5 * self.incMight - target.defence*(1-self.penRate),False)

                else:
                    tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Bloody Cleave on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 2.5 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
            else:
                if crit > self.cRate:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Bloody Cleave on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 1.8 * self.incMight - target.defence*(1-self.penRate),False)

                else:
                    tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Bloody Cleave on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Primal Force on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Primal Force on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Primal Force on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
    
    def ult(self, target):
        self.mana -= 100

        if self.health <= self.maxHealth/2:
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Rage Burst on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            target.takeDamage((self.attack * 2.8 + (self.maxHealth - self.health) / 8) * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)

        else:
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Rage Burst on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            target.takeDamage((self.attack * 2.8) * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
            self.health -= 40
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")

class Paladin(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 110

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen

        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Smite on" + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Smite on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.7 * self.incMight - target.defence*(1-self.penRate) + self.maxHealth * 0.005, False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Smite on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.7 * self.incMight * self.cDmg - target.defence*(1-self.penRate) + self.maxHealth * 0.005, True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Guiding Bolt on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Guiding Bolt on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 1.7 * self.incMight - target.wisdom*(1-self.penRate) + self.maxHealth * 0.005, False)
        
            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Guiding Bolt on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 1.7 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate) + self.maxHealth * 0.005, True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def takeDamage(self, damage, crit):
        self.health -= (damage*(1-self.dmgReduction))
        self.mana += 5 * self.manaRegen
        if crit == True:
            if damage < 1:
                self.health -= 1
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + "1" + Style.RESET_ALL + " damage!")
            else:
                self.health -= (damage*(1-self.dmgReduction))
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + str(round(damage*(1-self.dmgReduction), 2)) + Style.RESET_ALL + " damage!")
        else:
            if damage < 1:
                self.health -= 1
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken 1 damage!")
            else:
                self.health -= (damage*(1-self.dmgReduction))
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + str(round(damage*(1-self.dmgReduction), 2)) + " damage!")
        if self.health <= 0:
            playing = False

        self.health += (self.maxHealth * 0.005)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " recovered " + str(self.maxHealth * 0.005) + " health!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def ult(self, target):
        self.mana -= 110
        self.dmgReduction += 0.05
        self.health += 25
        self.maxHealth += 100

        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Radiant Decree, gaining 25 Health, 100 Max Health and +5% Damage Taken Reduction!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")

class SecretKeeper(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 120

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Lancing Silver on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Lancing Silver on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Lancing Silver on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Offensive Analysis on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            self.penRate += 0.05
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " gained +5% Penetration Rate!")
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Offensive Analysis on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(0.8-self.penRate), False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Offensive Analysis on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(0.8-self.penRate), True)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
            
    def ult(self, target):
        self.mana -= 120
        crit = random.randint(1, 100)
        self.penRate += 0.25

        if crit > self.cRate:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Voice in the Mind on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +25% Penetration Rate!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight - target.wisdom*(0.7-self.penRate), False)
        
        else:
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Voice in the Mind on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +25% Penetration Rate!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight * self.cDmg - target.wisdom*(0.7-self.penRate), True)

class Alchemist(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 120
    
    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Transmutation Blade on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Transmutation Blade on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Transmutation Blade on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
    
    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen

        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Potion Flurry on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if self.potions >= 1:
                crit -= 15
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumes a potion to gain temporary Critical Rate +15%!")
                self.potions -= 1
            
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Potion Flurry on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate), False)
            
            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Potion Flurry on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate), True)            
                self.potions += 1
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " brewed a potion!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def potion(self, target):
        crit = random.randint(1, 100)
        self.mana += 25 * self.manaRegen
        
        if crit > self.cRate:
            self.health += 80
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used a potion and recovered 80 health!")
        
        else:
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            self.health += (80 * self.cDmg)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used a potion and recovered " + Fore.RED + str(80 * self.cDmg) + Style.RESET_ALL + " health!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        self.potions -= 1
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

        if self.contaminated == True:
            self.poisoned(target)
            self.poisonTurns += 1

    def ult(self, target):
        self.mana -= 120
        self.potions += 3
        self.intelligence += 2
        self.cRate += 10
        
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Magnum Opus, brewing 3 potions, gaining +2 Intelligence and +10% Critical Rate!")

class Ranger(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 140
    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Steel Wind Strike on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            self.cDmg += 0.1
            
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Steel Wind Strike on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +10% Critical Damage!")
                target.takeDamage(self.attack * 1.8 * self.incMight - target.defence*(1-self.penRate), False)
            
            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Steel Wind Strike on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +10% Critical Damage!")
                target.takeDamage(self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
    
    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Spectral Quiver on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Spectral Quiver on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Spectral Quiver on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def ult(self, target):
        self.mana -= 140
        crit = random.randint(1, 100)
        self.cDmg += 0.25
        self.cRate += 5
        
        if crit > self.cRate:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Fatal Flicker on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +5% Critical Rate and +25% Critical Damage!")
            target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate), False)
        
        else:
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Fatal Flicker on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +5% Critical Rate and +25% Critical Damage!")
            target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)

class Executioner(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 130

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Beheading on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if target.health <= target.maxHealth*0.3:
                if crit > self.cRate:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Beheading on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage((self.attack * 2 + target.maxHealth * 0.05) * self.incMight - target.defence*(1-self.penRate), False)
                
                else:
                    tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Beheading on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage((self.attack * 2 + target.maxHealth * 0.05) * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)
            
            else:
                if crit > self.cRate:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Beheading on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 1.4 * self.incMight - target.defence*(1-self.penRate), False)
            
                else:
                    tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Beheading on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 1.4 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)
        
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Hand of Justice on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Hand of Justice on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Hand of Justice on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def ult(self, target):
        self.mana -= 130
        crit = random.randint(1, 100)
        
        if target.health <= target.maxHealth*0.5:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Death Sentence on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.7 * self.incMight + target.maxHealth * 0.1 - target.defence * (1-self.penRate), False)
            
            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Death Sentence on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.7 * self.incMight * self.cDmg + target.maxHealth * 0.1 - target.defence * (1-self.penRate), True)
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Death Sentence on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.7 * self.incMight - target.defence*(1-self.penRate), False)
           
            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Death Sentence on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.7 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)

class Vampire(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 140

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Sanguine Fangs on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Sanguine Fangs on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.8 * self.incMight - target.defence*(1-self.penRate), False)
                self.health += (self.attack * 1.8 * self.incMight - target.defence*(1-self.penRate))/4
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " restored " + str(round((self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate)))/4) + " health!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
            
            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Sanguine Fangs on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)
                self.health += (self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))/4
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " restored " + str(round((self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate)))/4) + " health!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10  * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Ray of Blood on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                self.health *= 0.95
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumed health to cast Ray of Blood on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
                target.takeDamage((self.intelligence * 2 + 20) * self.incMight - target.wisdom*(1-self.penRate), False)
        
            else:
                self.health *= 0.95
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumed health to cast Ray of Blood on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
                target.takeDamage((self.intelligence * 2 + 20) * self.incMight * self.cDmg - target.wisdom*(1-self.penRate), True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def ult(self, target):
        self.mana -= 140
        crit = random.randint(1, 100)
        
        if crit > self.cRate:
            self.health *= 0.95
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumed health to cast Blood Moon Rising on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
            target.takeDamage((self.intelligence * 3 + 40) * self.incMight - target.wisdom*(1-self.penRate), False)
      
        else:
            self.health *= 0.95
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumed health to cast Blood Moon Rising on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(self.health) + " health left!")
            target.takeDamage((self.intelligence * 3 + 40) * self.incMight * self.cDmg - target.wisdom*(1-self.penRate), True)

class FogWalker(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 110

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Concealed Dagger on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Concealed Dagger on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Concealed Dagger on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Miasma on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Miasma on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", decreasing their accuracy by 1%!")
                target.takeDamage(self.intelligence * 1.8 * self.incMight - target.wisdom*(1-self.penRate), False)
                target.accuracy -= 1

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Miasma on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", decreasing their accuracy by 3%!")
                target.takeDamage(self.intelligence * 1.5 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate), True)
                target.accuracy -= 3
            tprint(Fore.YELLOW + target.name + Style.RESET_ALL + " has " + str(target.accuracy) + "% accuracy!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
        
    def ult(self, target):
        self.mana -= 110
        crit = random.randint(1, 100)

        if crit > self.cRate:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Smoke and Mirrors on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", decreasing their accuracy by 5%!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight - target.wisdom*(1-self.penRate), False)
            target.accuracy -= 3

        else:
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Smoke and Mirrors on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", decreasing their accuracy by 5%!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate), True)
            target.accuracy -= 5
        tprint(Fore.YELLOW + target.name + Style.RESET_ALL + " has " + str(target.accuracy) + "% accuracy!")

class Spellblade(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 90

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 30 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Mana Edge on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Mana Edge on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.6 * self.incMight - target.defence*(1-self.penRate), False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Mana Edge on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.6 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Overclock on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumes mana to cast Overclock on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate) + round(self.mana * 0.3, 2), False)
                self.mana = round(self.mana*0.7, 2)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumes mana to cast Overclock on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate) + round(self.mana * 0.3, 2), True)
                self.mana = round(self.mana*0.7, 2)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
    
    def ult(self, target):
        time.sleep(0.8)
        ultType = tinput("Which ultimate do you want to cast? 1. Arcane Flash or 2. Esoteric Epitaph ")
        if ultType == "1":
            self.mana -= 90
            crit = random.randint(1, 100)
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Arcane Flash on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2.3 * self.incMight - target.defence*(1-self.penRate)*0.5, False)
    
            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Arcane Flash on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2.3 * self.incMight * self.cDmg - target.defence*(1-self.penRate)*0.5, True)
                
        elif ultType == "2":
            self.mana -= 90
            self.attack += 1
            self.intelligence += 1
            self.manaRegen += 0.1
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Esoteric Epitaph, gaining +1 Attack and Intelligence, and +10% Mana Regeneration Rate!")
            
class Drunkard(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 140

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " bashes " + Fore.YELLOW + target.name + Style.RESET_ALL + "'s skull in!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " bashes " + Fore.YELLOW + target.name + Style.RESET_ALL + "'s skull in!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " bashes " + Fore.YELLOW + target.name + Style.RESET_ALL + "'s skull in!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " tosses beer at " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " tosses beer at " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " tosses beer at " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def potion(self, target):
        originalHealth = self.health
        self.health += 50
        self.mana += 30 * self.manaRegen
        self.attack += 1
        self.dmgReduction += 0.01
        self.accuracy -= 4

        if self.health > self.maxHealth:
            self.health = self.maxHealth
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " drank some beer and recovered " + str(self.health - originalHealth) + " health!")

        else:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " drank some beer and recovered 50 health!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " gained +1 Attack, +1% Damage Taken Reduction, and 5% Critical Hit Rate, but lost 4% Accuracy!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
        self.potions -= 1

        if self.contaminated == True:
            self.poisoned(target)
            self.poisonTurns += 1

    def ult(self,target):
        self.mana -= 160
        self.potions += 2
        crit = random.randint(1, 100)
        
        if crit > self.cRate:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Drunken Frenzy on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining 2 bottles of beer and consuming one of them!")
            self.potion()
            target.takeDamage(self.attack * 2.6 * self.incMight - target.defence*(1-self.penRate), False)

        else:
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Drunken Frenzy on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining 2 bottles of beer and consuming one of them!")
            self.potion()
            target.takeDamage(self.attack * 2.6 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)

class Acrobat(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 160
        self.swiftness = 0
        self.flatDmg = 0

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        self.swiftness += 1
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Pirouette on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining 1 stack of Swiftness!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Pirouette on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining 1 stack of Swiftness!")
                target.takeDamage(self.attack * 1.6 * self.incMight - target.defence*(1-self.penRate) + self.flatDmg, False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Pirouette on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining 1 stack of Swiftness!")
                target.takeDamage(self.attack * 1.6 * self.incMight * self.cDmg - target.defence*(1-self.penRate) + self.flatDmg, True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Song of Twirling on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Song of Twirling on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Song of Twirling on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def ult(self,target):
        self.mana -= 160
        self.flatDmg += 10
        self.accuracy += self.swiftness*3
        
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Swirling Steps on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", consuming all stacks of Swiftness, gaining increased Accuracy and Flat Damage +10!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(self.accuracy) + "% accuracy!")

        for i in range(0,self.swiftness,2):
            crit = random.randint(1, 100)
            hit = random.randint(1, 100)
            
            if hit > self.accuracy:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
            
            else:
                if crit > self.cRate:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 1.3 * self.incMight - target.defence*(1-self.penRate) + self.flatDmg, False)

                else:
                    tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 1.3 * self.incMight * self.cDmg - target.defence*(1-self.penRate) + self.flatDmg, True)
            self.flatDmg += 1
        self.swiftness = 0

class Puppeteer(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 130
        self.puppets = 1
    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Weaving Blade on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Weaving Blade on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 0.8 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Weaving Blade on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 0.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

        for i in range(self.puppets):
            crit = random.randint(1, 100)
            hit = random.randint(1, 100)
            
            if hit > self.accuracy:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s puppet attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s puppet missed!")
            
            else:
                if crit > self.cRate:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s puppet attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 1.3 * self.incMight - target.defence*(1-self.penRate), False)

                else:
                    tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s puppet attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.attack * 1.3 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Dancing Strings on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Dancing Strings on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 0.8 * self.incMight - target.wisdom*(1-self.penRate), False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Dancing Strings on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * 0.8 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate), True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

        for i in range(self.puppets):
            crit = random.randint(1, 100)
            hit = random.randint(1, 100)
            
            if hit > self.accuracy:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s puppet casts a cantrip on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s puppet missed!")
            
            else:
                if crit > self.cRate:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s puppet casts a cantrip on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.intelligence * 1.3 * self.incMight - target.wisdom*(1-self.penRate), False)

                else:
                    tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s puppet casts a cantrip on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                    target.takeDamage(self.intelligence * 1.3 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate), True)

    def ult(self,target):
        self.mana -= 130
        self.puppets += 1
        self.attack += 2
        self.intelligence += 2

        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Masquerade of the Collective, creating 1 puppet, gaining +2 Attack and Intelligence!")

class Gambler(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 110

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Ace Up The Sleeve on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Ace Up The Sleeve on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Ace Up The Sleeve on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 90)
        hit = random.randint(1, 100)
        dice = random.randint(1,6)
        self.mana += 2 * self.manaRegen * dice
        
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " rolled a " + str(dice) + "!")

        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts All In on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts All In on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * dice / 2 * self.incMight - target.wisdom*(1-self.penRate), False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts All In on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.intelligence * dice / 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate), True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
    
    def ult(self, target):
        dice = random.randint(1,6)
        self.mana -= 110
        self.intelligence += dice
        self.manaRegen += dice/10
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has rolled a " + str(dice) + "!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Loaded Dice, gaining +" + str(dice) + " Intelligence and +" + str(dice) + "0% Mana Regeneration Rate!")

class Proxy(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 120
        self.tentacleDmg = 12
        self.ritualProgress = 1
        self.potions = 6

    def tentacle(self, target):
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " commands a tentacle to attack " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
        target.takeDamage(self.tentacleDmg * 2 * self.incMight - target.defence*(1-self.penRate),False)

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Sacrificial Strike on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            self.health = round(self.health * 0.95, 0)
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumes health to use Sacrificial Strike on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", increasing Tentacle Damage by 1!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " consumes health to use Sacrificial Strike on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", increasing Tentacle Damage by 1!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
        self.tentacleDmg += 1
        self.tentacle(target)

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Abyss Command on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Abyss Command on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", restoring " + str(self.tentacleDmg) + " health!")
                target.takeDamage(self.intelligence * 1.7 * self.incMight - target.wisdom*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Abyss Command on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", restoring " + str(self.tentacleDmg) + " health!")
                target.takeDamage(self.intelligence * 1.7 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate),True)
            self.health += self.tentacleDmg
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
        self.tentacle(target)

    def potion(self, target):
        originalHealth = self.health
        self.health += 60
        self.mana += 30 * self.manaRegen

        if self.health > self.maxHealth:
            self.health = self.maxHealth
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used a potion and recovered " + str(self.health - originalHealth) + " health, gaining 1 Ritual Progress!")

        else:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used a potion and recovered 60 health, gaining 1 Ritual Progress!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
        self.potions -= 1
        self.ritualProgress += 1

        if self.contaminated == True:
            self.poisoned(target)
            self.poisonTurns += 1

    def ult(self,target):
        self.mana -= 120
        self.tentacleDmg += 4
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Eldritch Ritual, gaining +4 Tentacle Damage and Commanding Tentacles to attack!")
        if self.ritualProgress >= 3:
            for i in range(self.ritualProgress):
                self.tentacle(target)
            self.ritualProgress -= 3

class Agent(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 100

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Silent Takedown on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Silent Takedown on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", triggering 1 round of Poison!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Silent Takedown on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", triggering 1 round of Poison!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
            target.poisonTurns -= 1
            target.poisoned(self)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Honeyed Words on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")
        
        else:
            target.poisonTurns += 1
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Honeyed Words on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", inflicting 1 round of Poison!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Honeyed Words on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", inflicting 1 round of Poison!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")
    
    def ult(self, target):
        self.mana -= 100
        self.wisdom += 4
        target.poisonTurns += 5
        target.contaminated = True
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " used Assasin's Mark, gaining +4 Wisdom, inflicting the Contaminated status and applying 5 rounds of Poison!")
    
class Bladesinger(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 120
        self.flyingSwords = 3
        self.swordHealth = 30
    
    def takeDamage(self, damage, crit):
        self.mana += 5 * self.manaRegen
        if self.flyingSwords >= 1:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s Flying Sword sacrifices itself to reduce Damage Taken!")
            self.swordHealth -= damage
            if self.swordHealth <= 0:
                damage = self.swordHealth * -1
                if crit == True:
                    if damage < 1:
                        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + "0" + Style.RESET_ALL + " damage!")
                    else:
                        self.health -= (damage*(1-self.dmgReduction))
                        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + str(round(damage*(1-self.dmgReduction), 2)) + Style.RESET_ALL + " damage!")
                else:
                    if damage < 1:
                        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken 0 damage!")
                    else:
                        self.health -= (damage*(1-self.dmgReduction))
                        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + str(round(damage*(1-self.dmgReduction), 2)) + " damage!")
                self.flyingSwords -= 1
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(self.flyingSwords) + " Flying Swords left!")
                self.swordHealth = 20
            else:
                if crit == True:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + "0" + Style.RESET_ALL + " damage!")
                else:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken 0 damage!")
        else:
            if crit == True:
                if damage < 1:
                    self.health -= 1
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + "1" + Style.RESET_ALL + " damage!")
                else:
                    self.health -= (damage*(1-self.dmgReduction))
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + Fore.RED + str(round(damage*(1-self.dmgReduction), 2)) + Style.RESET_ALL + " damage!")
            else:
                if damage < 1:
                    self.health -= 1
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken 1 damage!")
                else:
                    self.health -= (damage*(1-self.dmgReduction))
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has taken " + str(round(damage*(1-self.dmgReduction), 2)) + " damage!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(round(self.health, 2)) + " health left!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Sweeping Bladesong on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " missed!")

        else:
            if crit > self.cRate:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Sweeping Bladesong on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.8 * self.incMight - target.defence*(1-self.penRate),False)

            else:
                tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Sweeping Bladesong on " + Fore.YELLOW + target.name + Style.RESET_ALL + "!")
                target.takeDamage(self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate),True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

        if self.flyingSwords >= 1:
            crit = random.randint(1, 100)
            hit = random.randint(1, 100)
            
            if hit > self.accuracy:
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s Flying Sword attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +1% Incantation Might!")
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s Flying Sword missed!")
            
            else:
                if crit > self.cRate:
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s Flying Sword attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +1% Incantation Might!")
                    target.takeDamage(self.attack * 0.6 * self.incMight - target.defence*(1-self.penRate), False)

                else:
                    tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
                    tprint(Fore.YELLOW + self.name + Style.RESET_ALL + "'s Flying Sword attacks " + Fore.YELLOW + target.name + Style.RESET_ALL + ", gaining +1% Incantation Might!")
                    target.takeDamage(self.attack * 0.6 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)
                self.flyingSwords -= 1
                self.incMight += 0.01
                tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(self.flyingSwords) + " Flying Swords left!")

    def cantrip(self, target):
        self.mana += 20 * self.manaRegen
        self.flyingSwords += 2
        self.dmgReduction += 0.01
    
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " casts Phalanx Command, creating 2 Flying Swords and gaining +1% Damage Taken Reduction!")
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(self.flyingSwords) + " Flying Swords left!")

        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + Fore.BLUE + str(round(self.mana, 2)) + Style.RESET_ALL + " mana!")

    def ult(self,target):
        self.mana -= 120
        self.flyingSwords += 5
        crit = random.randint(1, 100)
        
        if crit > self.cRate:
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Lacerating Deluge on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", creating 5 Flying Swords!")
            target.takeDamage(self.attack * self.flyingSwords * 0.3 * self.incMight - target.defence*(1-self.penRate), False)

        else:
            tprint(Fore.RED + "Critical hit!" + Style.RESET_ALL)
            tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " uses Lacerating Deluge on " + Fore.YELLOW + target.name + Style.RESET_ALL + ", creating 5 Flying Swords!")
            target.takeDamage(self.attack * self.flyingSwords * 0.3 * self.incMight * self.cDmg - target.defence*(1-self.penRate), True)
        tprint(Fore.YELLOW + self.name + Style.RESET_ALL + " has " + str(self.flyingSwords) + " Flying Swords left!")
#You have 25 skill points. Each skill point increases Attack/Defence/Intelligence/Wisdom by 1, Health by 100, Critical Rate by 10, Critical Damage by 0.2, Incantation Might/Penetration/Damage Taken Reduction by 0.1.
#Base Attack/Defence/Intelligence/Wisdom is 10, Health is 1000, Critical Rate is 10, Critical Damage is 2, Incantation Might is 1, Penetration Rate/Damage Taken Reduction is 0, Accuracy is 80
#Max Attack/Defence/Intelligence/Wisdom is 20, Health is 2000, Critical Rate is 70, Critical Damage is 3, Incantation Might is 2, Penetration Rate is 1, Damage Taken Reduction is 0.5, Accuracy is 80

CHARACTER_CLASSES = {
    "barbarian": Barbarian,
    "paladin": Paladin,
    "secret keeper": SecretKeeper,
    "alchemist": Alchemist,
    "ranger": Ranger,
    "executioner": Executioner,
    "vampire": Vampire,
    "fog walker": FogWalker,
    "spellblade": Spellblade,
    "drunkard": Drunkard,
    "acrobat": Acrobat,
    "puppeteer": Puppeteer,
    "gambler": Gambler,
    "proxy": Proxy,
    "agent": Agent,
    "bladesinger": Bladesinger
}

players = []

for i in range(2):
    player_name = input(f"Enter player {i + 1}'s name: ")

    class_name = input("Enter the player's class: ").strip().lower()
    while class_name not in CHARACTER_CLASSES:
        print(f"Unknown character class '{class_name}'. Chose one from: ", class_name)
        for character_class in CHARACTER_CLASSES.keys():
            print(character_class)

        class_name = input("Enter the player's class: ").strip().lower()

    SP = 30
    print("You have 30 skill points. Each skill point increases Attack/Defence/Intelligence/Wisdom by 1, Health by 100, Critical Rate by 10%, Critical Damage by 20%, Penetration Rate/Mana Regeneration Rate by 10%, Incantation Might/Damage Taken Reduction by 5%.")
    print("Base Attack/Defence/Intelligence/Wisdom is 10, Health is 1000, Critical Rate is 10%, Critical Damage is 100%, Incantation Might/Mana Regeneration Rate is 100%, Penetration Rate/Damage Taken Reduction is 0%, Mana Regeneration Rate is 100%")
    print("Max Attack/Defence/Intelligence/Wisdom is 20, Health is 1500, Critical Rate is 80%, Critical Damage is 200%, Incantation Might is 150%, Penetration Rate is 100%, Damage Taken Reduction is 25%, Mana Regeneration Rate is 200%")

    health = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Health? Each skill point increases Health by 100: ")
    while health.isnumeric() != True or int(health) > 5 or int(health) < 0 or int(health) > SP:
        health = input("Please input a valid number ")
    health = int(health)
    SP -= health

    attack = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Attack? Each skill point increases Attack by 1: ")
    while attack.isnumeric() != True or int(attack) > 10 or int(attack) < 0 or int(attack) > SP:
        attack = input("Please input a valid number ")
    attack = int(attack)
    SP -= attack

    defence = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Defence? Each skill point increases Defence by 1: ")
    while defence.isnumeric() != True or int(defence) > 10 or int(defence) < 0 or int(defence) > SP:
        defence = input("Please input a valid number ")
    defence = int(defence)
    SP -= defence

    intelligence = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Intelligence? Each skill point increases Intelligence by 1: ")
    while intelligence.isnumeric() != True or int(intelligence) > 10 or int(intelligence) < 0 or int(intelligence) > SP:
        intelligence = input("Please input a valid number ")
    intelligence = int(intelligence)
    SP -= intelligence

    wisdom = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Wisdom? Each skill point increases Wisdom by 1: ")
    while wisdom.isnumeric() != True or int(wisdom) > 10 or int(wisdom) < 0 or int(wisdom) > SP:
        wisdom = input("Please input a valid number ")
    wisdom = int(wisdom)
    SP -= wisdom

    cRate = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Critical Rate? Each skill point increases Critical Rate by 10%: ")
    while cRate.isnumeric() != True or int(cRate) > 7 or int(cRate) < 0 or int(cRate) > SP:
        cRate = input("Please input a valid number ")
    cRate = int(cRate)
    SP -= cRate

    cDmg = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Critical Damage? Each skill point increases Critical Damage by 20%: ")
    while cDmg.isnumeric() != True or int(cDmg) > 5 or int(cDmg) < 0 or int(cDmg) > SP:
        cDmg = input("Please input a valid number ")
    cDmg = int(cDmg)
    SP -= cDmg

    penRate = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Penetration Rate? Each skill point increases Penetration Rate by 10%: ")
    while penRate.isnumeric() != True or int(penRate) > 10 or int(penRate) < 0 or int(penRate) > SP:
        penRate = input("Please input a valid number ")
    penRate = int(penRate)
    SP -= penRate

    incMight = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Incantation Might? Each skill point increases Incantation Might by 5%: ")
    while incMight.isnumeric() != True or int(incMight) > 5 or int(incMight) < 0 or int(incMight) > SP:
        incMight = input("Please input a valid number ")
    incMight = int(incMight)
    SP -= incMight

    dmgReduction = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Damage Taken Reduction? Each skill point increases Damage Taken Reduction by 5%: ")
    while dmgReduction.isnumeric() != True or int(dmgReduction) > 5 or int(dmgReduction) < 0 or int(dmgReduction) > SP:
        dmgReduction = input("Please input a valid number ")
    dmgReduction = int(dmgReduction)
    SP -= dmgReduction

    manaRegen = input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Mana Regeneration Rate? Each skill point increases Mana Regeneration Rate by 10%: ")
    while manaRegen.isnumeric() != True or int(manaRegen) > 10 or int(manaRegen) < 0 or int(manaRegen) > SP:
        manaRegen = input("Please input a valid number ")
    manaRegen = int(manaRegen)
    SP -= manaRegen

    players.append(CHARACTER_CLASSES[class_name](player_name, (health*100 + 1000), (attack + 10), (defence + 10), (intelligence + 10), (wisdom + 10), (cRate * 7.5 + 15), (cDmg * 0.2 + 2), (penRate * 0.1), (incMight * 0.05 + 1), (dmgReduction*0.05), (manaRegen * 0.1 + 1), 80, 3))
#(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
# randomly decide who goes first
if random.randint(0, 2) == 0:
    players = players[::-1]

playing = True
while playing:
    for attacker, defender in (players, players[::-1]):
        while True: 
            action = tinput("It is " + Fore.YELLOW + attacker.name + Style.RESET_ALL + "'s turn. What do you want to do? 1. Strike 2. Cantrip 3. Ultimate 4. Potion ")
            if action == "1":
                attacker.strike(defender)
                break
            elif action == "2":
                attacker.cantrip(defender)
                break
            elif action == "3":
                if attacker.mana >= attacker.ultMana:
                    attacker.ult(defender)
                    break
                else:
                    tprint("Please input a valid action")
            elif action == "4":
                if attacker.potions > 0:
                    attacker.potion(defender)
                    break
                else:
                    tprint("Please input a valid action")
            else:
                tprint("Please input a valid action")
            
        if attacker.poisonTurns >= 1:
            attacker.poisoned(defender)
            attacker.poisonTurns -= 1

        if defender.health <= 0:
            tprint(Fore.YELLOW + attacker.name + Style.RESET_ALL + " has won the battle!")
            playing = False
            break
