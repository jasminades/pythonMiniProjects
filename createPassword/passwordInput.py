import string

def is_valid_password(pwd):
    has_number=any(char.isdigit() for char in pwd)
    has_special_char = any(char in string.punctuation for char in pwd)

    return len(pwd)>5 and has_number and has_special_char


def get_valid_password():
    while True:
        password = input("Enter a password: ")
        if is_valid_password(password):
            confirmation = input("Do you want to confirm this password? (yes/no) ").lower()
            if confirmation =="yes":
                return password
            elif confirmation == "no":
                print("Generating a new password...")
            else:
                print("Invalid input. Please enter 'yes' or 'no' ")
        elif len(password)<=5:
            print("The password must have more than 5 characters ")
        else:
            print("The password must contain at least one number and special character")


password = get_valid_password()
print("The password you entered is:  " , password)