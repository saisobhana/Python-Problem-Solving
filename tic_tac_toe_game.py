import random
is_continue = True
while is_continue:
    user_input = input("To roll the Dice please enter Y : If you don't want to roll the dice please enter N : ").upper()
    if user_input == "Y":
        a = random.randint(1,6)
        b = random.randint(1,6)
        print("First Random Number is",a)
        print("Second Random Number is",b)
    elif user_input == "N":
        print("Thank you for Playing dear user")
        is_continue = False
    else:
        print("Invalid Choice please input valid choice dear user")
       
