class chatbook:
  def __init__(self):
    self.username = ''
    self.password =  '' 
    self.loggedin = False
    # hum chaahte h ki jaise hi user kare toh usko option dekhne lage
    self.menu() 
    '''self me object ka reference hai ya address hota h islye hum menu ko call 
    kr pa rahe h kyuki jab bhi object banega toh menu call ho jayega aur user ko 
    options dekhne ko milenge''' 

  def menu(self):
    user_input = input("""Welocome to Chatbook! how would you like to proceed?
          1. Press 1 to SignUp
          2. Press 2 to Sighin
          3. Press to write a post
          4. Press 4 to message a friend
          5. Press any other key to exit""")

    if user_input == '1': 
    # jab bhi user input lete h toh wo string ke form me hota h islye humne '1' likha h
      self.signup()
    elif user_input == '2':
      pass
    elif user_input == '3':
      pass
    elif user_input == '4':
      pass
    else:
      print("Thank you for visiting Chatbook! See you soon.")
      exit()
  


obj = chatbook()
    