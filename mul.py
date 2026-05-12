# multilevel inheritance

class Grandparent:
  def __init__(self, name):
    self.name = name

  def tell_story(self):
    print(f"{self.name} is telling a story.")

# intermediate class
class Parent(Grandparent):
  def work(self):
    print(f"{self.name} is working.")

# derived class
class Child(Parent):
  def play(self):
    print(f"{self.name} is playing.")

# creating an object of the child class
child = Child("Charlie")
child.tell_story() # inherited from Grandparent
child.work() # inherited from Parent
child.play() # method of Child class