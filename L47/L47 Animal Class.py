from abc import ABC
# create a base class
class Animal(ABC):
    # abstract method
    # should be implemented by all subclasses
    def move(self):
        pass

# sub classes
class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

# create objects
R = Human()
R.move()

K = Snake()
K.move()

D = Dog()
D.move()

L = Lion()
L.move()