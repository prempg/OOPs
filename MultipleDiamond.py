# Multiple Inheritance with Diamond Problem

# Common base class
class A:
    def __init__(self, name):
      self.name = name

    def greet(self):
      print(f"Hello from class A, I am {self.name}.")

# intermediate class 1
class B(A):
    def greet(self):
      print(f"Hello from class B, I am {self.name}.")
      super().greet() # calling the greet method of class A

# intermediate class 2
class C(A):
    def greet(self):
      print(f"Hello from class C, I am {self.name}.")
      super().greet() # calling the greet method of class A

# derived class
class D(B, C):
    def greet(self):
      print(f"Hello from class D, I am {self.name}.")
      super().greet() # calling the greet method of class B and C

# creating an object of the derived class
d = D("Charlie")
d.greet() 
# method of class D, B, C and A will be called in order due to MRO (Method Resolution Order)
