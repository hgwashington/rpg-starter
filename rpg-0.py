
import random





class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self,enemy):
        enemy.health -= self.power
    def alive(self):
       return self.health > 0
    def print_status(self):
        print(self.health) 

class Medic(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
    def recover(self):
        heal = random.randint(1,5)
        if heal == 5:
            self.health += 2

class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
    def attack(self, enemy):
        crit = random.randint(1,5)
        if crit == 1:
            enemy.health -= self.power * 2
            print("Critical Hit!")
        else:
            enemy.health -= self.power

class Phantom(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
    def ghost(self):
        phase = random.randint(1,10)
        if phase == 1:
            self.health == 1

class Undead(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
    def NeverDie(self):
        if self.health == 0:
            self.health += 666

       
hunter = Hero(100, 5)
medic = Medic(25, 5)
shadow = Phantom(25, 1)
runner = Character(20, 2)

gunter = Character(25,2)
wizard = Character(40, 4)
zombie = Undead(1, 2)

while gunter.alive() == True and hunter.alive()== True:

        print("You have %d health and %d power." % (hunter.health, hunter.power))
        print("The goblin has %d health and %d power." % (gunter.health, gunter.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin            
            gunter.health -= hunter.power
            print("You do %d damage to the goblin." % hunter.power)
            if gunter.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if gunter.alive() == True:
            # Goblin attacks hero
            hunter.health -= gunter.power
            print("The goblin does %d damage to you." % gunter.power)
            if hunter.alive() == False:
                print("You are dead.")




















##################################################
# Muted code#

"""class Goblin():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self,enemy):
        enemy.health -= self.power
    def alive(self):
       return self.health > 0
    def print_status(self):
        print(self.health) """

