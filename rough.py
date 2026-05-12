lst = [1,2,3]
my_str = " Hello World"
my_int = 155

print(type(lst))
print(type(my_str))
print(type(my_int))

a = 'x'
b = 'y'
print(a+b) # concatenation

from oops_proj import chatbook
user_1 = chatbook()

# function
a1 = len(lst)
print(a1)

# method
# user_1.sendMsg() 
# print(user_1.__name)
print(user_1._chatbook__name)
'''ye method h kyunki ye class ke andar defined h aur usko class ke 
object se call kiya h '''


# getter and setter method
print(user_1.get_name())
print(user_1.set_name("John Doe"))
print(user_1.get_name())


# static methods
print(user_1.id)

user_2 = chatbook()
print(user_2.id)

user_3 = chatbook()
print(user_3.id)

# using static method directly from class rather than object
chatbook.set_id(10)

user_2 = chatbook()
print(user_2.id)

user_3 = chatbook()
print(user_3.id)

