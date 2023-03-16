class Robot:
    def __init__(self, name, color, weight, looking_at):
        self.name = name
        self.color = color
        self.weight = weight
        self.looking_at = looking_at

    def introduce_self(self):
        print("My name is " + self.name)

class Person:
    def __init__(self, name, personality, is_sitting, robot_owned):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        self.robot_owned = robot_owned

    def sitDown(self):
        if self.is_sitting == False:
            self.is_sitting == True

    def standUp(self):
        if self.is_sitting == True:
            self.is_sitting == False

r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)

p1 = Person("Alice", "aggresive", False, r2)
p2 = Person("BeckY", "talkative", True, r1)

r1.introduce_self()


