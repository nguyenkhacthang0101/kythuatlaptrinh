class Animal:
    def__init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def__init__(self):
        Animal__init__(self)
        print("Dog created")

    def WhoAmI(self):
        print("Dog")

    def bark(self):
        print("Wood")

d = Dog()
d.WhoAmI()
d.eat()
d.bark()
        

            
