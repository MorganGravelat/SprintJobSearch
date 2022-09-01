class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal): # Inherits from Animal
    def __init__(self):
        super().__init__() #The constructor is the same as the animal constructor, the class also inherits methods

    def breathe(self):
        super().breathe() #The breathe method is the same as the animal breathe method
        print("Blub, blub") #Unique twist on the animal class method breathe

    def swim(self):
        print("I'm swimming")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
