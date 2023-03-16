class Guitar:
    def __init__(self, n_strings = 6):
        self.n_strings = n_strings
        self.play()
    def play(self):
        print("pam pam")

class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__(n_strings = 8)
        self.colour = ("#000000", "#FFFFFF")
        self.cost = 50
    def playlouder(self):
        print("pam pam".upper())
    def __secret(self):
        print("this guitar actually cost me $", self.cost, "only!")

class BassGuitar(Guitar):
    pass

my_guitar = ElectricGuitar()
my_guitar.playlouder()
print("Child Class: ", + my_guitar.n_strings)
print("Parent Class: ", + Guitar().n_strings)
my_guitar._ElectricGuitar__secret()

print(BassGuitar(4).n_strings)