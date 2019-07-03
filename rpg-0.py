
import random





class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.inv = []
        self.armor = False
        self.evade = 0
    def attack(self,enemy):
        if enemy.armor == True:
            enemy.health -= (self.power - 2)
        else:
            enemy.health -= self.power
    def alive(self):
       return self.health > 0
    def print_status(self):
        print(self.health) 
    def give_armor(self):
        self.armor = True
    def dodge(self, enemy):
        move = random.randint(1,10)
        if move == 10:
            self.health += enemy.attack

    #def add_item(self, item_name):


class Medic(Character):
    def __init__(self, health, power, coins):
        super().__init__(health, power)
        self.coins = coins
    def recover(self):
        heal = random.randint(1,5)
        if heal == 5:
            self.health += 2

class Hero(Character):
    def __init__(self, health, power, coins):
        super().__init__(health, power)
        self.coins = coins
    def attack(self, enemy):
        crit = random.randint(1,5)
        if crit == 1:
            self.power *= 2

class Phantom(Character):
    def __init__(self, health, power, coins):
        super().__init__(health, power)
        self.coins = coins
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
class Enemy(Character):
     def __init__(self, health, power, bounty):
        super().__init__(health, power)
        self.bounty = bounty

       
hunter = Hero(100, 5, 10)
medic = Medic(25, 5, 10)
shadow = Phantom(25, 1, 10)
#runner = Character(20, 2)

gunter = Enemy(25, 2, 3)
wizard = Enemy(40, 4, 6)
zombie = Undead(2, 2)


'''allies = [hunter, medic, shadow]
enemies = [gunter, wizard, zombie]'''



def battle(friend, enemy):
    while enemy.alive() == True and friend.alive()== True:
        if friend.coins > 1:
            shop = input('''Would you like to shop?
            Type yes or no:  ''')
            if shop == 'yes':
                chance = random.randint(1,10)
                what = input('''What would you like?
                Type 1 for super tonic
                Type 2 for armor
                Type 3 for evade
                Type 4 for steroids
                Type 5 for serum
                Type 6 for swap
                What will it be?: ''')
                if what == '1':
                    friend.health += 10
                    friend.coins -= 2
                elif what == '2':
                    friend.give_armor()
                    friend.coins -= 2
                elif what == '3':
                    if chance == 10:
                        friend.health += enemy.power
                    
                elif what == '4':
                    friend.power += 5
                    friend.health /= 2 
                    friend.coins -= 2
                    print("_________________")
                    print("That's a slippery slope, but okay dude. I mean, its your body...")
                    print("_________________")
                elif what == '5':
                    friend.power += 2
                    friend.health += 2
                    friend.coins -= 2
                    print("_________________")
                    print("Not as potent as roids, but not as deadly either...")
                    print("_________________")
                elif what == '6':
                    friend.health == enemy.health and enemy.health == friend.health
                    friend.power == enemy.power and enemy.power == friend.power
                    friend.coins -= 2
                    
                else:
                    print("We dont have that here")
                

            elif shop == 'no':
                print("_________________")
                print('')
                print('Good Luck out there!')
                print("_________________")


        print("You have %d health and %d power." % (friend.health, friend.power))
        print("The enemy has %d health and %d power." % (enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks enemy           
            enemy.health -= friend.power
            print("You do %d damage to the enemy." % friend.power)
        if enemy.health <= 0:
            print("You just won %d coins!" % enemy.bounty)
            friend.coins += enemy.bounty
            print("The enemy is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye, you coward.")
            break
        # else:
        #     print("Invalid input %r" % user_input)

        if enemy.alive() == True:
                # enemy attacks hero
            friend.health -= enemy.power
            print("The enemy does %d damage to you." % enemy.power)
        if friend.alive() == False:
            print("You are dead.")
battle(hunter, wizard)






# while True:
#     battle(hunter, wizard)
#     shop = input('''Would you like to shop?
#     Type yes or no:  ''')
#     if shop == 'yes':
#         what = input('''What would you like?
#         Type 1 for super tonic
#         Type 2 for armor
#         Type 3 for evade''')
#         if what == '1':
#             hunter.health += 10
#             hunter.coins -= 2
#         elif what == '2':
#             hunter.give_armor()
#             hunter.coins -= 2
#         elif what == '3':
#             print('Too Bad')
#     elif shop == 'no':
#         print('Good Luck out there!')
#         break
            
    
      



# shop = input('''Would you like to shop?
# Type yes or no:  ''')
# if shop == 'yes':
#     what = input('''What would you like?''')












