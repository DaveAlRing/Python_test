import random

class Character:
    def __init__(self, name):
        self.name = name
        self.strength = 5
        self.intelligence = 5
        self.agility = 5
        self.charisma = 5
        self.luck = 5
    
    def intro(self):
        bio = f"""I am {self.name}.
            My stats are as follows:
            Strength: {self.strength}
            Intelligence: {self.intelligence}
            Agility: {self.agility}
            Charisma: {self.charisma}
            Luck: {self.luck}"""
        return bio
        
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name)
        self.job = "Paladin"
        
        return self.job
    
    def stat(self):
        self.strength += random.randint(1,3)
        self.intelligence += random.randint(2,4)
        self.agility += random.randint(-1,1)
        self.charisma += random.randint(-1,1)
        self.luck += random.randint(0,2)
        
        return (self.strength,
                self.intelligence, self.agility,
                self.charisma, self.luck)
    
    def intro(self):
        return super().intro() + (f"\n I am a {self.job}!")
        
class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"I'm a Mage named {self.name}.")
        
dave = Paladin("Dave")
teagan = Character("Teagan")

print(dave.intro())