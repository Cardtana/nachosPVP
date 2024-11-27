import random
import time
from sys import stdout

def tprint(text):
    time.sleep(0.8)
    for c in text:
        print(c,end="")
        stdout.flush()
        time.sleep(0.05)
    print()
    
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

    def takeDamage(self, damage):
        self.mana += 5 * self.manaRegen
        if damage < 1:
            self.health -= 1
            tprint(self.name + " has taken 1 damage!")
        else:
            self.health -= (damage*(1-self.dmgReduction))
            tprint(self.name + " has taken " + str(round(damage*(1-self.dmgReduction), 2)) + " damage!")
        tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " attacks " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate))

            else:
                tprint("Critical hit!")
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate))
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " casts a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate))

            else:
                tprint("Critical hit!")
                tprint(self.name + " casts a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def potion(self):
        originalHealth = self.health
        self.health += 120
        self.mana += 30 * self.manaRegen

        if self.health > self.maxHealth:
            self.health = self.maxHealth
            tprint(self.name + " used a potion and recovered " + str(self.health - originalHealth) + " health!")

        else:
            tprint(self.name + " used a potion and recovered 120 health!")
        tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")
        self.potions -= 1

    def ult(self):
        pass

class Barbarian(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 100

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " attacks " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if self.health <= self.maxHealth/2:
                crit -= 30
                if crit > self.cRate:
                    tprint(self.name + " attacks " + target.name + "!")
                    target.takeDamage(self.attack * 3 * self.incMight - target.defence*(1-self.penRate))

                else:
                    tprint("Critical hit!")
                    tprint(self.name + " attacks " + target.name + "!")
                    target.takeDamage(self.attack * 3 * self.incMight * self.cDmg - target.defence*(1-self.penRate))
            else:
                if crit > self.cRate:
                    tprint(self.name + " attacks " + target.name + "!")
                    target.takeDamage(self.attack * 1.8 * self.incMight - target.defence*(1-self.penRate))

                else:
                    tprint("Critical hit!")
                    tprint(self.name + " attacks " + target.name + "!")
                    target.takeDamage(self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def ult(self, target):
        self.mana -= 100

        if self.health <= self.maxHealth/2:
            tprint("Critical hit!")
            tprint(self.name + " used Primal Rage on " + target.name + "!")
            target.takeDamage((self.attack * 5 + (self.maxHealth - self.health) / 3) * self.incMight * self.cDmg - target.defence*(1-self.penRate))

        else:
            tprint("Critical hit!")
            tprint(self.name + " used Primal Rage on " + target.name + "!")
            target.takeDamage((self.attack * 5) * self.incMight * self.cDmg - target.defence*(1-self.penRate))
            self.health -= 40
            tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")

class Paladin(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 110

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen

        if hit > self.accuracy:
            tprint(self.name + " attacks " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate) + self.maxHealth * 0.02)

            else:
                tprint("Critical hit!")
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate) + self.maxHealth * 0.02)
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")
    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " casts a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate) + self.maxHealth * 0.02)
        
            else:
                tprint("Critical hit!")
                tprint(self.name + " casts a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate) + self.maxHealth * 0.02)
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def takeDamage(self, damage):
        self.health -= (damage*(1-self.dmgReduction))
        self.mana += 5 * self.manaRegen
        if damage < 1:
            self.health -= 1
            tprint(self.name + " has taken 1 damage!")
        else:
            self.health -= (damage*(1-self.dmgReduction))
            tprint(self.name + " has taken " + str(round(damage*(1-self.dmgReduction), 2)) + " damage!")
        tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
        if self.health <= 0:
            playing = False

        self.health += (self.maxHealth * 0.005)
        tprint(self.name + " recovered " + str(self.maxHealth * 0.005) + " health!")
        tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def ult(self, target):
        self.mana -= 110
        self.dmgReduction += 0.05
        self.health += 50
        self.maxHealth += 200

        tprint(self.name + " used Radiant Decree, gaining 50 Health, 200 Max Health and +5% Damage Taken Reduction!")
        tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")

class SecretKeeper(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 120

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            self.penRate += 0.05
            tprint(self.name + " gained +5% Penetration Rate!")
            if crit > self.cRate:
                tprint(self.name + " casts a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(0.8-self.penRate))

            else:
                tprint("Critical hit!")
                tprint(self.name + " casts a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(0.8-self.penRate))
            tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")
            
    def ult(self, target):
        self.mana -= 120
        crit = random.randint(1, 100)
        self.penRate += 0.5

        if crit > self.cRate:
            tprint(self.name + " casts Voice in the Mind on " + target.name + ", gaining +50% Penetration Rate!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight - target.wisdom*(0.7-self.penRate))
        
        else:
            tprint("Critical hit!")
            tprint(self.name + " casts Voice in the Mind on " + target.name + ", gaining +50% Penetration Rate!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight * self.cDmg - target.wisdom*(0.7-self.penRate))

class Alchemist(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 120

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen

        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if self.potions >= 1:
                crit -= 30
                tprint(self.name + " consumes a potion to gain temporary Critical Rate +30%!")
                self.potions -= 1
            
            if crit > self.cRate:
                tprint(self.name + " casts a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate))
            
            else:
                tprint("Critical hit!")
                tprint(self.name + " casts a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))            
                self.potions += 1
                tprint(self.name + " brewed a potion!")
            tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def potion(self):
        crit = random.randint(1, 100)
        self.mana += 25 * self.manaRegen
        
        if crit > self.cRate:
            self.health += 80
            tprint(self.name + " used a potion and recovered 80 health!")
        
        else:
            self.health += (80 * self.cDmg)
            tprint(self.name + " used a potion and recovered " + str(80 * self.cDmg) +  " health!")
        tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
        self.potions -= 1
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def ult(self, target):
        self.mana -= 120
        self.potions += 3
        self.intelligence += 8
        self.cRate += 20
        
        tprint(self.name + " used Magnum Opus, brewing 3 potions, gaining 8 Intelligence and +20% Critical Rate!")

class Ranger(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 140
    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " attacks " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            self.cDmg += 0.1
            
            if crit > self.cRate:
                tprint(self.name + " attacks " + target.name + ", gaining +10% Critical Damage!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate))
            
            else:
                tprint("Critical hit!")
                tprint(self.name + " attacks " + target.name + ", gaining +10% Critical Damage!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate))
            tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def ult(self, target):
        self.mana -= 140
        crit = random.randint(1, 100)
        self.cDmg += 0.8
        self.cRate += 30
        
        if crit > self.cRate:
            tprint(self.name + " used Fatal Flicker on " + target.name + ", gaining +30% Critical Rate and +80% Critical Damage!")
            target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate))
        
        else:
            tprint("Critical hit!")
            tprint(self.name + " used Fatal Flicker on " + target.name + ", gaining +30% Critical Rate and +80% Critical Damage!")
            target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate))

class Executioner(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 130

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " attacks " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if target.health <= target.maxHealth*0.3:
                if crit > self.cRate:
                    tprint(self.name + " attacks " + target.name + "!")
                    target.takeDamage((self.attack * 2 + target.maxHealth * 0.3) * self.incMight - target.defence*(1-self.penRate))
                
                else:
                    tprint("Critical hit!")
                    tprint(self.name + " attacks " + target.name + "!")
                    target.takeDamage((self.attack * 2 + target.maxHealth * 0.3) * self.incMight * self.cDmg - target.defence*(1-self.penRate))
            
            else:
                if crit > self.cRate:
                    tprint(self.name + " attacks " + target.name + "!")
                    target.takeDamage(self.attack * 1.4 * self.incMight - target.defence*(1-self.penRate) + target.health * 0.1)
            
                else:
                    tprint("Critical hit!")
                    tprint(self.name + " attacks " + target.name + "!")
                    target.takeDamage(self.attack * 1.4 * self.incMight * self.cDmg - target.defence*(1-self.penRate) + target.health * 0.1)
        
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def ult(self, target):
        self.mana -= 130
        crit = random.randint(1, 100)
        
        if target.health <= target.maxHealth*0.5:
            if crit > self.cRate:
                tprint(self.name + " uses Invitation to a Beheading on " + target.name + "!")
                target.takeDamage(self.attack * 3 * self.incMight + target.maxHealth * 0.1 - target.defence * (1-self.penRate))
            
            else:
                tprint("Critical hit!")
                tprint(self.name + " uses Invitation to a Beheading on " + target.name + "!")
                target.takeDamage(self.attack * 3 * self.incMight * self.cDmg + target.maxHealth * 0.1 - target.defence * (1-self.penRate))
        else:
            if crit > self.cRate:
                tprint(self.name + " uses Invitation to a Beheading on " + target.name + "!")
                target.takeDamage(self.attack * 3 * self.incMight - target.defence*(1-self.penRate))
           
            else:
                tprint("Critical hit!")
                tprint(self.name + " uses Invitation to a Beheading on " + target.name + "!")
                target.takeDamage(self.attack * 3 * self.incMight * self.cDmg - target.defence*(1-self.penRate))

class Vampire(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana == 110

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " attacks " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 1.8 * self.incMight - target.defence*(1-self.penRate))
                self.health += (self.attack * 1.8 * self.incMight - target.defence*(1-self.penRate))/4
                tprint(self.name + " restored " + str((self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))/4) + " health!")
                tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
            
            else:
                tprint("Critical hit!")
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))
                self.health += (self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))/4
                tprint(self.name + " restored " + str((self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))/4) + " health!")
                tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10  * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                self.health *= 0.95
                tprint(self.name + " consumed health to cast a cantrip on " + target.name + "!")
                tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
                target.takeDamage((self.intelligence * 2 + 20) * self.incMight - target.wisdom*(1-self.penRate))
        
            else:
                self.health *= 0.95
                tprint("Critical hit!")
                tprint(self.name + " consumed health to cast a cantrip on " + target.name + "!")
                tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
                target.takeDamage((self.intelligence * 2 + 20) * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def ult(self, target):
        self.mana -= 110
        crit = random.randint(1, 100)
        
        if crit > self.cRate:
            self.health *= 0.95
            tprint(self.name + " consumed health to cast Blood Moon Rising on " + target.name + "!")
            tprint(self.name + " has " + str(round(self.health, 2)) + " health left!")
            target.takeDamage((self.intelligence * 3 + 40) * self.incMight - target.wisdom*(1-self.penRate))
      
        else:
            self.health *= 0.95
            tprint("Critical hit!")
            tprint(self.name + " consumed health to cast Blood Moon Rising on " + target.name + "!")
            tprint(self.name + " has " + str(self.health) + " health left!")
            target.takeDamage((self.intelligence * 3 + 40) * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))

class FogWalker(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 110
    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " casts a cantrip on " + target.name + ", decreasing their accuracy by 1%!")
                target.takeDamage(self.intelligence * 1.5 * self.incMight - target.wisdom*(1-self.penRate))
                target.accuracy -= 1

            else:
                tprint("Critical hit!")
                tprint(self.name + " casts a cantrip on " + target.name + ", decreasing their accuracy by 3%!")
                target.takeDamage(self.intelligence * 1.5 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))
                target.accuracy -= 3
            tprint(target.name + " has " + str(target.accuracy) + "% accuracy!")
            tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")
        
    def ult(self, target):
        self.mana -= 110
        crit = random.randint(1, 100)

        if crit > self.cRate:
            tprint(self.name + " casts Miasma on " + target.name + ", decreasing their accuracy by 5%!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight - target.wisdom*(1-self.penRate))
            target.accuracy -= 1

        else:
            tprint("Critical hit!")
            tprint(self.name + " casts Miasma on " + target.name + ", decreasing their accuracy by 5%!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))
            target.accuracy -= 5
        tprint(target.name + " has " + str(target.accuracy) + "% accuracy!")

class Spellblade(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
        self.ultMana = 90

    def strike(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 30 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " attacks " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 2 * self.incMight - target.defence*(1-self.penRate))

            else:
                tprint("Critical hit!")
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 2 * self.incMight * self.cDmg - target.defence*(1-self.penRate))
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")

    def cantrip(self, target):
        crit = random.randint(1, 100)
        hit = random.randint(1, 100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " consumes mana to cast a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate) + round(self.mana * 0.3, 2))
                self.mana = round(self.mana*0.7, 2)

            else:
                tprint("Critical hit!")
                tprint(self.name + " consumes mana to cast a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate) + round(self.mana * 0.3, 2))
                self.mana = round(self.mana*0.7, 2)
        tprint(self.name + " has " + str(round(self.mana, 2)) + " mana!")
    
    def ult(self, target):
        time.sleep(0.8)
        ultType = input("Which ultimate do you want to cast? Arcane Flash (1) or Esoteric Epitaph (2) ")
        if ultType == "1":
            self.mana -= 90
            crit = random.randint(1, 100)
            if crit > self.cRate:
                tprint(self.name + " casts Arcane Flash on " + target.name + "!")
                target.takeDamage(self.attack * 2.3 * self.incMight - target.defence*(1-self.penRate)*0.5)
    
            else:
                tprint("Critical hit!")
                tprint(self.name + " casts Arcane Flash on " + target.name + "!")
                target.takeDamage(self.attack * 2.3 * self.incMight * self.cDmg - target.defence*(1-self.penRate)*0.5)
                
        elif ultType == "2":
            self.mana -= 90
            self.attack += 6
            self.intelligence += 6
            self.manaRegen += 0.5
            tprint(self.name + " casts Esoteric Epitaph, gaining +6 Attack and Intelligence, and +50% Mana Regeneration Rate!")
            

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
    "spellblade": Spellblade
}

players = []

for i in range(2):
    player_name = input(f"Enter player {i + 1}'s name: ")

    class_name = input("Enter the player's class: ").strip().lower()
    while class_name not in CHARACTER_CLASSES:
        print(f"Unknow character class '{class_name}'. Chose one from: ", class_name)
        for character_class in CHARACTER_CLASSES.keys():
            print(character_class)

        class_name = input("Enter the player's class: ").strip().lower()

    # TODO: add way to chose stats
    SP = 30
    print("You have 30 skill points. Each skill point increases Attack/Defence/Intelligence/Wisdom by 1, Health by 100, Critical Rate by 10, Critical Damage by 0.2, Incantation Might/Penetration/Damage Taken Reduction by 0.1.")
    print("Base Attack/Defence/Intelligence/Wisdom is 10, Health is 1000, Critical Rate is 10, Critical Damage is 2, Incantation Might is 1, Penetration Rate/Damage Taken Reduction is 0, Accuracy is 80")
    print("Max Attack/Defence/Intelligence/Wisdom is 20, Health is 2000, Critical Rate is 70, Critical Damage is 3, Incantation Might is 2, Penetration Rate is 1, Damage Taken Reduction is 0.5, Accuracy is 80")

    health = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Health? "))
    while health > 10 or health < 0 or health > SP:
        health = int(input("Please input a valid number "))
    SP -= health

    attack = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Attack? "))
    while attack > 10 or attack < 0 or attack > SP:
        attack = int(input("Please input a valid number "))
    SP -= attack

    defence = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Defence? "))
    while defence > 10 or defence < 0 or defence > SP:
        defence = int(input("Please input a valid number "))
    SP -= defence

    intelligence = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Intelligence? "))
    while intelligence > 10 or intelligence < 0 or intelligence > SP:
        intelligence = int(input("Please input a valid number "))
    SP -= intelligence

    wisdom = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Wisdom? "))
    while wisdom > 10 or wisdom < 0 or wisdom > SP:
        wisdom = int(input("Please input a valid number "))
    SP -= wisdom

    cRate = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Critical Rate? "))
    while cRate > 8 or cRate < 0 or cRate > SP:
        cRate = int(input("Please input a valid number "))
    SP -= cRate

    cDmg = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Critical Damage? "))
    while cDmg > 10 or cDmg < 0 or cDmg > SP:
        cDmg = int(input("Please input a valid number "))
    SP -= cDmg

    penRate = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Penetration Rate? "))
    while penRate > 10 or penRate < 0 or penRate > SP:
        penRate = int(input("Please input a valid number "))
    SP -= penRate

    incMight = int(input("You have " + str(SP)+ " skill points. How many skill poinsts do you want to invest in Incantation Might? "))
    while incMight > 10 or incMight < 0 or incMight > SP:
        incMight = int(input("Please input a valid number "))
    SP -= incMight

    dmgReduction = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Damage Taken Reduction? "))
    while dmgReduction > 5 or dmgReduction < 0 or dmgReduction > SP:
        dmgReduction = int(input("Please input a valid number "))
    SP -= dmgReduction

    manaRegen = int(input("You have " + str(SP)+ " skill points. How many skill points do you want to invest in Mana Regeneration Rate? "))
    while manaRegen > 10 or manaRegen < 0 or manaRegen > SP:
        manaRegen = int(input("Please input a valid number "))
    SP -= manaRegen
        
    players.append(CHARACTER_CLASSES[class_name](player_name, (health*100 + 1000), (attack + 10), (defence + 10), (intelligence + 10), (wisdom + 10), (cRate * 7.5 + 15), (cDmg * 0.1 + 2), (penRate * 0.1), (incMight * 0.1 + 1), (dmgReduction*0.05), (manaRegen * 0.1 + 1), 80, 3))
#(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, manaRegen, accuracy, potions)
# randomly decide who goes first
if random.randint(0, 2) == 0:
    players = players[::-1]

playing = True
while playing:
    for attacker, defender in (players, players[::-1]):
        while True: 
            time.sleep(0.8)
            action = input("It is " + attacker.name + "'s turn. What do you want to do? 1. Strike 2. Cantrip 3. Ultimate 4. Potion ")
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
                    attacker.potion()
                    break
                else:
                    tprint("Please input a valid action")
            else:
                tprint("Please input a valid action")
            
        if defender.health <= 0:
            tprint(attacker.name + " has won the battle!")
            playing = False
            break
