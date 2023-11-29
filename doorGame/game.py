import random

def doorgame():
    life = 5
    while life > 0:
        door = random.randint(1,5)
        print("Door: ", door)
        print("Life: ", life)
        life -= 1


        guess = input("Enter a guess of door: ")

        try:
            guess=int(guess)
        except ValueError:
            print("Invalid input. Please enter a number ")
            continue

        if guess != door:
            if life>0:
                print("Guess Again!")
                continue
            else:
                print("You lost all lives! The correct door was " +  str(door))

        else:
            print("Well done, you managed to escape! ")

        print("Do you want to play again?")
        answer = input("Yes or No ").lower()[0]

        if answer=="y":
            life = 5
        else:
            life = 0
    else:
        print("Game over")

doorgame()

