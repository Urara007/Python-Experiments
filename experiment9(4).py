class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        # Overriding the parent method
        print("The Dog barks")

class Cat(Animal):
    def sound(self):
        # Overriding the parent method
        print("The Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()