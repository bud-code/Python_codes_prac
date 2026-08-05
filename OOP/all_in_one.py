from abc import ABC, abstractmethod

# Abstraction
class Animal(ABC):

    def __init__(self, name):
        self.name = name          # Encapsulation of data with behavior
        self.__age = 5            # Private attribute

    def get_age(self):            # Controlled access (Encapsulation)
        return self.__age

    @abstractmethod
    def sound(self):
        pass

# Inheritance
class Dog(Animal):

    # Polymorphism (implementation differs from other animals)
    def sound(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):

    # Polymorphism
    def sound(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Kitty")

dog.sound()
cat.sound()

print(dog.get_age())