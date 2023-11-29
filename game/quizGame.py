print("Welcome to the game!!")

playing = input("Do you want to start the game? ").lower()

counter=0;

if playing != "yes":
    print("Okay, bye! ")
    quit()
print("Let's start! ")


answer = input("1. What does CPU stand for? ")
if answer.lower()  == "central processing unit":
    print("Correct!")
    counter+=1
else:
    print("Incorrect!")


answer = input("2. What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")



answer = input("3. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")



answer = input("4. What does PSU stand for? ")
if answer.lower()  == "power supply unit":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")


answer = input("5. What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")


answer = input("6. What does SSL stand for? ")
if answer.lower() == "secure sockets layer":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")


answer = input("7. What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")


print("Good job! Your score is: " , counter)
print("You got " + str((counter/7) * 100) + "%" )