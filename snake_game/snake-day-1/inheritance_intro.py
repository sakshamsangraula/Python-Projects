class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale exhale")



class Fish(Animal):
    # use the constructor to call the super class constructor
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("breathing under water")

    def swim(self):
        print("Moving in water")

fish1 = Fish()
print(fish1.num_eyes)
fish1.breathe()
fish1.swim()