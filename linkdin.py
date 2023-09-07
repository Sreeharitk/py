'''''
food = input("What's your favorite food: ")
if food == "biriyani":
    print("Yup thats amazing")
else:
    print("Yuck thats not it")
print("thanks for playing")
'''''
'''''
def car_wash(amount):
    if amount == 8:
        print("Its a normal car wash")
    elif amount == 12:
        print("Its a premium car wash")
car_wash(12)
'''''
'''''
def withdraw(current,amount):
    if (current>=amount):
        current = current - amount
    else:
        print("insufficient balance")
    return current

balance = withdraw(10,80)

print("The balance is ", balance)

if balance <= 50:
    print("Need to make a deposit above 50 rs")
else:
    print("Have a nice day")
'''''
'''''
def favorite_city(name):
    print("one of my favorite cities is ", name)
favorite_city("Kozhikode")
favorite_city("Kannur")
favorite_city("palakad")
'''''
