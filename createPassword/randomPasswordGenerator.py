import random
import string


def generatePassword(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation



    characters = letters
    if numbers:
        characters += digits

    if special_characters:
        characters += special_chars

    pwd = ""
    meets_criteria = False
    has_number=False
    has_special_char=False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special_char= True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = has_special_char and meets_criteria

    return pwd



min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers? (y/n) ").lower()=="y"
has_special_chars = input("Do you want to have special characters? (y/n) ").lower()=="y"
pwd=generatePassword(min_length, has_number, has_special_chars)
print("The generated password is: " ,  pwd)