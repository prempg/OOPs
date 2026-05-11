# initiate the class
class employee:
  '''
  special method/ magic method/ dunder method
  * data ya attributes define karne ke liye jo dunder method use hota hai
  wo hai __init__ (constructor)
  '''
  def __init__(self):
    self.id = 123
    self.salary = 500000
    self.designation = 'SDE' 

  def travel(self,destination):
    print(f'Travelling to {destination}')

# create an object/ instance of the class
sam = employee()

print(sam.id)
sam.travel('Bangalore')
