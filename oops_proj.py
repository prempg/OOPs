class chatbook:
  def __init__(self):
    self.username = ''
    self.password =  '' 
    self.loggedin = False 
    '''agar ye false h toh aage ka functionalities use nahi kar sakte h user jab tak 
    sign in nahi karta tab tak usko ye options nahi dekhne ko milenge'''


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
          5. Press any other key to exit
                       
                     ->  """)

    if user_input == '1': 
    # jab bhi user input lete h toh wo string ke form me hota h islye humne '1' likha h
      self.signup()
    elif user_input == '2':
      self.signin()
    elif user_input == '3':
      self.my_post()
    elif user_input == '4':
      self.sendMsg()
    else:
      print("Thank you for visiting Chatbook! See you soon.")
      exit()
  
  def signup(self):
    email = input("Enter your email here -> ")
    password = input("Enter your password here -> ")

    ''' uper ke do input se do user input le rahe h email aur password ke form 
    me aur usko variables me store kar rahe h(jo ki upper ke do variables h)'''

    self.username = email 
    self.password = password
    print("Congratulations! You have successfully signed up for Chatbook!")
    print("\n")
    self.menu()

  def signin(self):
    ''' if user is already signed up then only they can sign in otherwise 
    they have to sign up first '''
    if self.username == '' and self.password == '':
      print("You have not signed up yet! Please sign up first by selecting option 1.")
      self.menu()
    else:
      uname = input("Enter your email here -> ")
      password = input("Enter your password here -> ")

      if self.username == uname and self.password == password:
        print("Congratulations! You have successfully signed in to Chatbook!")
        self.loggedin = True
      else:
        print("Invalid email or password! Please try again.")
    print("\n")
    self.menu()

  def my_post(self):
    if self.loggedin: # Ture ho toh user post kar sakta h(longgdin)
      post = input("Write your post here -> ")
      print(f"Your post has been published on Chatbook! {post}")
    else:
      print("You need to sign in first to write a post.")
    print("\n")
    self.menu()

  def sendMsg(self):
    # friend ka id h ya nahi ye bhi check kr sakte h but humne simple sa code likha h
    if self.loggedin:
      friend = input("Enter your friend's name here -> ")
      msg = input("Write your message here -> ")
      print(f"Your message has been sent to {friend}! {msg}")
    else:
      print("You need to sign in first to send a message.")
    print("\n")
    self.menu()


# obj = chatbook()
    