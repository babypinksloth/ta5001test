import random

class Character:
    def __init__(self):
        self.name = "Greg"
        self.hp = 100
        self.strength = 7
        self.intelligence = 5
        self.wisdom = 6
        
        self.critchance = 15 
        
        self.is_alive = True
        
    def display_stats(self):
        print (f"\t  {self.name}" )
        print (f"Health : {self.hp}" )
        print (f"Strength : {self.strength}" )
        print (f"Intelligence : {self.intelligence}" )
        print (f"Wisdom : {self.wisdom}" )
    
    def check_status(self):
        if self.hp <= 0:
            self.is_alive = False

    def attack_with_critchance(self, target):
        damage = self.strength 
        is_crit = random.randint(1,100)
        
        if is_crit <= self.critchance:
            damage *= 2
            print ("*****Hit was Critical!*****")
            
        target.hp -= damage
        target.check_status()
             
    def attack(self, target):
        target.hp -= self.strength
        target.check_status()

class Hero (Character):
    def __init__(self, hero_name):
        super().__init__()
        
        if hero_name:
            self.name = hero_name
            
    def display_stats(self):
        print (f"###### Hero Stats ########")
        super().display_stats()
        print (f"##########################")
        
class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.hp = 20
    
    def display_stats(self):
        print (f"###### Enemy Stats #######")
        super().display_stats()
        print (f"##########################")

# ----- 
name = input("What is your name?: ")

player = Hero(name)
orc = Enemy()
isGameRunning = True
    
player.display_stats()
print ("\n")
orc.display_stats()

while isGameRunning:
    command = input("An Orc Stands before you! What would you like to do? \n").lower()
    
    match command:
        case "attack":
            player.attack(orc)
        case "run" | "flee":
            print ("You are a coward")
            isGameRunning = False
        case "defend":
            pass
        case "exit":
            break
        case _:
            print ("Invalid Command!")
            continue

    if not orc.is_alive:
        print (f"The Orc {orc.name} was defeated! You Win! ")
        isGameRunning = False
    else:
        print (f"The Health of Orc {orc.name} is now {orc.hp}!")
        #### The Orc Takes their turn ####
        print (f"The Orc {orc.name} swings at the Hero!")
        orc.attack(player)
        print (f"You are hit! Your Health is now {player.hp}")
        #################################
        
    if not player.is_alive:
        print (f"The Orc {orc.name} has bested you! You are Dead!")
        isGameRunning = False

print ("Game Over!")