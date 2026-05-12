# Single or Basic Inheritance

class Parent:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Hello, I am {self.name}.")

# derived class
class Child(Parent):  
  def play(self):
    print(f"{self.name} is playing.")

# creating an object of the child class
child = Child("Alice")
child.greet() # inherited method from Parent class
child.play() # method of Child class
