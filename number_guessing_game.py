import random
num = random.randint(1, 100)

tries = 0 
user = 0 

while user != num:
    user = input("Enter your guess: ")
    user = int(user)

    if user > num:
        print("Too high")
        tries = tries + 1
    elif user < num:
        print("Too low")
        tries = tries + 1
    else:
        print("You got it! it only took you", tries, "tries!")
        

