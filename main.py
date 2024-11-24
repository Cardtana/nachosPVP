import random
import time
global playing
playing = True
def tprint(text):
    time.sleep(0.8)
    print(text)
class Character:
    def __init__(self,name,health,attack,defence,intelligence,wisdom,cRate,cDmg,penRate,incMight,dmgReduction,manaRegen,accuracy,potions):
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

    def takeDamage(self,damage):
        self.mana += 5 * self.manaRegen
        self.health -= (damage*(1-self.dmgReduction))
        tprint(self.name + " has taken " + str(round(damage*(1-self.dmgReduction),2)) + " damage!")
        tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def strike(self,target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def cantrip(self,target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def potion(self):
        originalHealth = self.health
        self.health += 120
        self.mana += 30 * self.manaRegen

        if self.health > self.maxHealth:
            self.health = self.maxHealth
            tprint(self.name + " used a potion and recovered " + str(self.health - originalHealth) + " health!")

        else:
            tprint(self.name + " used a potion and recovered 120 health!")
        tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
        tprint(self.name + " has " + str(self.mana) + " mana!")
        self.potions -= 1

    def ult(self):
        pass

class Barbarian(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana == 100

    def strike(self, target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
        tprint(self.name + " has " + str(self.mana) + " mana!")

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
            tprint(self.name + " has " + str(round(self.health,2)) + " health left!")

class Paladin(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana == 110

    def strike(self,target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
        tprint(self.name + " has " + str(self.mana) + " mana!")
    def cantrip(self,target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def takeDamage(self, damage):
        self.health -= (damage*(1-self.dmgReduction))
        self.mana += 5 * self.manaRegen
        tprint(self.name + " has taken " + str(round(damage*(1-self.dmgReduction),2)) + " damage!")
        tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
        if self.health <= 0:
            playing = False

        self.health += (self.maxHealth * 0.03)
        tprint(self.name + " recovered " + str(self.maxHealth * 0.03) + " health!")
        tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def ult(self,target):
        self.mana -= 110
        self.dmgReduction += 0.3
        self.health += 50
        self.maxHealth += 80

        tprint(self.name + " used Radiant Decree, gaining 50 Health, 80 Max Health and +30% Damage Taken Reduction!")
        tprint(self.name + " has " + str(round(self.health,2)) + " health left!")

class SecretKeeper(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana == 120

    def cantrip(self, target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
            tprint(self.name + " has " + str(self.mana) + " mana!")
            
    def ult(self,target):
        self.mana -= 120
        crit = random.randint(1,100)
        self.penRate += 0.5

        if crit > self.cRate:
            tprint(self.name + " casts Voice in the Mind on " + target.name + ", gaining +50% Penetration Rate!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight - target.wisdom*(0.7-self.penRate))
        
        else:
            tprint("Critical hit!")
            tprint(self.name + " casts Voice in the Mind on " + target.name + ", gaining +50% Penetration Rate!")
            target.takeDamage(self.intelligence * 2.5 * self.incMight * self.cDmg - target.wisdom*(0.7-self.penRate))

class Alchemist(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana == 120

    def cantrip(self, target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
            tprint(self.name + " has " + str(self.mana) + " mana!")

    def potion(self):
        crit = random.randint(1,100)
        self.mana += 25 * self.manaRegen
        
        if crit > self.cRate:
            self.health += 80
            tprint(self.name + " used a potion and recovered 80 health!")
        
        else:
            self.health += (80 * self.cDmg)
            tprint(self.name + " used a potion and recovered " + str(80 * self.cDmg) +  " health!")
        tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
        self.potions -= 1
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def ult(self,target):
        self.mana -= 120
        self.potions += 3
        self.intelligence += 8
        self.cRate += 20
        
        tprint(self.name + " used Magnum Opus, brewing 3 potions, gaining 8 Intelligence and +20% Critical Rate!")

class Ranger(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana == 140
    def strike(self, target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
            tprint(self.name + " has " + str(self.mana) + " mana!")

    def ult(self,target):
        self.mana -= 140
        crit = random.randint(1,100)
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
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana == 130

    def strike(self, target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def ult(self, target):
        self.mana -= 130
        crit = random.randint(1,100)
        
        if target.health <= target.maxHealth*0.5:
            if crit > self.cRate:
                tprint(self.name + " uses Invitation to a Beheading on " + target.name + "!")
                target.takeDamage(self.attack * 2.5 * self.incMight + target.maxHealth * 0.1 - target.defence * (1-self.penRate))
            
            else:
                tprint("Critical hit!")
                tprint(self.name + " uses Invitation to a Beheading on " + target.name + "!")
                target.takeDamage(self.attack * 2.5 * self.incMight * self.cDmg + target.maxHealth * 0.1 - target.defence * (1-self.penRate))
        else:
            if crit > self.cRate:
                tprint(self.name + " uses Invitation to a Beheading on " + target.name + "!")
                target.takeDamage(self.attack * 2.5 * self.incMight - target.defence*(1-self.penRate))
           
            else:
                tprint("Critical hit!")
                tprint(self.name + " uses Invitation to a Beheading on " + target.name + "!")
                target.takeDamage(self.attack * 2.5 * self.incMight * self.cDmg - target.defence*(1-self.penRate))

class Vampire(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana == 110

    def strike(self, target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
                tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
            
            else:
                tprint("Critical hit!")
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))
                self.health += (self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))/4
                tprint(self.name + " restored " + str((self.attack * 1.8 * self.incMight * self.cDmg - target.defence*(1-self.penRate))/4) + " health!")
                tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def cantrip(self, target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
        self.mana += 10  * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                self.health *= 0.95
                tprint(self.name + " consumed health to cast a cantrip on " + target.name + "!")
                tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
                target.takeDamage((self.intelligence * 2 + 20) * self.incMight - target.wisdom*(1-self.penRate))
        
            else:
                self.health *= 0.95
                tprint("Critical hit!")
                tprint(self.name + " consumed health to cast a cantrip on " + target.name + "!")
                tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
                target.takeDamage((self.intelligence * 2 + 20) * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def ult(self,target):
        self.mana -= 110
        crit = random.randint(1,100)
        
        if crit > self.cRate:
            self.health *= 0.95
            tprint(self.name + " consumed health to cast Blood Moon Rising on " + target.name + "!")
            tprint(self.name + " has " + str(round(self.health,2)) + " health left!")
            target.takeDamage((self.intelligence * 2.2 + 40) * self.incMight - target.wisdom*(1-self.penRate))
      
        else:
            self.health *= 0.95
            tprint("Critical hit!")
            tprint(self.name + " consumed health to cast Blood Moon Rising on " + target.name + "!")
            tprint(self.name + " has " + str(self.health) + " health left!")
            target.takeDamage((self.intelligence * 2.2 + 40) * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))

class FogWalker(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana = 110
    def cantrip(self,target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
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
        tprint(self.name + " has " + str(self.mana) + " mana!")
        
    def ult(self,target):
        self.mana -= 110
        crit = random.randint(1,100)

        if crit > self.cRate:
            tprint(self.name + " casts Miasma on " + target.name + ", decreasing their accuracy by 5%!")
            target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate))
            target.accuracy -= 1

        else:
            tprint("Critical hit!")
            tprint(self.name + " casts Miasma on " + target.name + ", decreasing their accuracy by 5%!")
            target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate))
            target.accuracy -= 5
        tprint(target.name + " has " + str(target.accuracy) + "% accuracy!")

class Spellblade(Character):
    def __init__(self, name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions):
        super().__init__(name, health, attack, defence, intelligence, wisdom, cRate, cDmg, penRate, incMight, dmgReduction, accuracy, potions)
        self.ultMana = 90

    def strike(self,target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
        self.mana += 30 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " attacks " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 1.7 * self.incMight - target.defence*(1-self.penRate))

            else:
                tprint("Critical hit!")
                tprint(self.name + " attacks " + target.name + "!")
                target.takeDamage(self.attack * 1.7 * self.incMight * self.cDmg - target.defence*(1-self.penRate))
        tprint(self.name + " has " + str(self.mana) + " mana!")

    def cantrip(self,target):
        crit = random.randint(1,100)
        hit = random.randint(1,100)
        self.mana += 10 * self.manaRegen
        
        if hit > self.accuracy:
            tprint(self.name + " casts a cantrip on " + target.name + "!")
            tprint(self.name + " missed!")
        
        else:
            if crit > self.cRate:
                tprint(self.name + " consumes mana to cast a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight - target.wisdom*(1-self.penRate) + round(self.mana * 0.3,2))
                self.mana = round(self.mana*0.7,2)

            else:
                tprint("Critical hit!")
                tprint(self.name + " consumes mana to cast a cantrip on " + target.name + "!")
                target.takeDamage(self.intelligence * 2 * self.incMight * self.cDmg - target.wisdom*(1-self.penRate) + round(self.mana * 0.3,2))
                self.mana = round(self.mana*0.7,2)
        tprint(self.name + " has " + str(self.mana) + " mana!")
    
    def ult(self,target):
        self.mana -= 90
        crit = random.randint(1,100)
        if crit > self.cRate:
            tprint(self.name + " casts Arcane Flash on " + target.name + "!")
            target.takeDamage(self.attack * 2.6 * self.incMight - target.defence*(1-self.penRate))

        else:
            tprint("Critical hit!")
            tprint(self.name + " casts Arcane Flash on " + target.name + "!")
            target.takeDamage(self.attack * 2.6 * self.incMight * self.cDmg - target.defence*(1-self.penRate))

#You have 25 skill points. Each skill point increases Attack/Defence/Intelligence/Wisdom by 1, Health by 100, Critical Rate by 10, Critical Damage by 0.2, Incantation Might/Penetration/Damage Taken Reduction by 0.1.
#Base Attack/Defence/Intelligence/Wisdom is 10, Health is 1000, Critical Rate is 10, Critical Damage is 2, Incantation Might is 1, Penetration Rate is 0, Accuracy is 80
#Max Attack/Defence/Intelligence/Wisdom is 20, Health is 2000, Critical Rate is 70, Critical Damage is 3, Incantation Might is 2, Penetration Rate is 1, Accutacy is 80

p1 = Character("Insert Name Here",1000,10,10,10,10,10,2,0,1,0,1,80,3) #Skill Points: 25, Choose class from classes declared above aside from "Character"
p2 = Character("Insert Name Here",1000,10,10,10,10,10,2,0,1,0,1,80,3) #Skill Points: 25, Choose class from classes declared above aside from "Character"

initiative = random.randint(1,2)
if initiative == 1:
    a1 = p1
    a2 = p2
else:
    a1 = p2
    a2 = p1

while playing:
    a1Action = True
    while a1Action:
        time.sleep(0.8)
        action = input("It is " + a1.name + "'s turn. What do you want to do? 1. Strike 2. Cantrip 3. Ultimate 4. Potion ")
        if action == "1":
            a1.strike(a2)
            break
        elif action == "2":
            a1.cantrip(a2)
            break
        elif action == "3":
            if a1.mana >= a1.ultMana:
                a1.ult(a2)
                break
            else:
                tprint("Please input a valid action")
        elif action == "4":
            if a1.potions > 0:
                a1.potion()
                break
            else:
                tprint("Please input a valid action")
        else:
            tprint("Please input a valid action")
        
    if a2.health <= 0:
        tprint(a1.name + " has won the battle!")
        playing = False
        break

    a2Action = True
    while a2Action:
        time.sleep(0.8)
        action = input("It is " + a2.name + "'s turn. What do you want to do? 1. Strike 2. Cantrip 3. Ultimate 4. Potion ")
        if action == "1":
            a2.strike(a1)
            break
        elif action == "2":
            a2.cantrip(a1)
            break
        elif action == "3":
            if a2.mana >= a2.ultMana:
                a2.ult(a1)
                break
            else:
                tprint("Please input a valid action")
        elif action == "4":
            if a2.potions > 0:
                a2.potion()
                break
            else:
                tprint("Please input a valid action")
        else:
            tprint("Please input a valid action")

    if a1.health <= 0:
        tprint(a2.name + " has won the battle!")
        playing = False
        break
