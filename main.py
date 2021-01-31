import random

def input_check(number):
        ######## Checking to see if input is number ######
    while True:
        try:
            #user_input = int(input(number))
            conv = int(number)
        except ValueError:
            print("Please enter a number 1-9")
            math_game()  #this needs to be removed.
        else:
            break
    return conv
        ##################################################

def rand_number():
    x = random.randint(1, 12)
    return x

def math_game():
    q = 0
    listing = []

    print("Multiplication Practice!")
    print("------------------------")
    print("Press ctrl-c to exit game")
    y = input("What number would you like to practice? ")
    
    while 1:
        user_input = input_check(y)
        x = rand_number()
        c = input_check(input(f"What is {user_input} * {x}? "))
        
        listing.append(f'{user_input} * {x}')
        answer = user_input * x
        if c == answer:
            print("correct")
        else:
            print("-----------Incorrect!  Lets practice!----------")
            print(f"{user_input} * {x} is {answer}")
            while q < 3:
                c = int(input(f"What is {user_input} * {x} = "))
                if c == answer:
                    print("correct")
                    q += 1
            print("-------------\nLets Continue!")

        print(listing)
math_game()