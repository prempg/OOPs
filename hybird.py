# hybrid
# hybrid inheritance me ek class do ya do se zyada class se inherit karti h
class Animal:
  def __init__(self, name):
    self.name = name

    def sound(self):
      print(f"{self.name} makes a sound")

# intermediate class 1 (hierarchical inheritance)
  class Mammal(Animal):
    def feed_milk(self):
      print(f"{self.name} feeds milk to its young ones.")

# intermediate class 2 (multiple inheritance)
class Bird(Animal):
  def fly(self):
    print(f"{self.name} can fly.")

# derived class (Multiple inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # calling the constructor of Mammal class

    def norturnal(self):
        print(f"{self.name} squeaks.")

# creating objects of the derived class
bat = Bat("Bruce")
bat.sound()  # calls the sound method of class Animal
bat.feed_milk()  # calls the feed_milk method of class Mammal
bat.fly()  # calls the fly method of class Bird
bat.norturnal()  # calls the norturnal method of class Bat