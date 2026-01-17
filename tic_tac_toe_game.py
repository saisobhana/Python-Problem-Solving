import random
is_continue = True
while is_continue:
    user_input = input("To roll the Dice please enter Y : If you don't want to roll the dice please enter N : ")
    if user_input == "Y" or user_input == "y":
        a = random.randint(1,6)
        b = random.randint(1,6)
        print("First Random Number is",a)
        print("Second Random Number is",b)
    elif user_input == "N" or user_input == "n":
        print("Thank you for Playing")
        is_continue = False
    else:
        print("Invalid Choice")
       
