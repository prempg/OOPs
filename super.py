# Super

# Base class
class Animal:
  def __init__(self, name):
    self.name = "Buddy"
  
  def speak(self):
    print(f"{self.name} makes a sound")

# Derived class 
class Dog(Animal):
  def __init__(self, breed):
    super().__init__() # calling the parent class constructor
    self.breed = breed
  
  def speak(self):
    super().speak() # calling the parent class method
    print(f"{self.name} barks. It is a {self.breed}.")
  
dog = Dog("Golden Retriever")
dog.speak()