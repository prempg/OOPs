# hirarchical inheritance me ek class multiple classes se inherit kar sakti h

# Base class 
class Parent:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Hello, I am {self.name}.")

# Derived class 1
class Child1(Parent):
  def play(self):
    print(f"{self.name} is playing.")

# Derived class 2
class Child2(Parent):
  def study(self):
    print(f"{self.name} is studying.")

# creating objects of the derived classes
child1 = Child1("Alice")
child2 = Child2("Bob")

child1.greet() # inherited method from Parent class
child1.play() # method of Child1 class

child2.greet() # inherited method from Parent class
child2.study() # method of Child2 class