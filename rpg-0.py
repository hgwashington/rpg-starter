"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""

'''def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2'''
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
    

hunter = Character(10, 5)
gunter = Character(6,2)

#hunter.attack(gunter)
#print(gunter.__dict__)







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
            if hunter.alive() ==True:
                print("You are dead.")