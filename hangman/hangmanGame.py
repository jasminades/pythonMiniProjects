import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)             # randomly chooses the word
    while '-' in word or ' ' in word:
        word = random.choice(words)         # so words with space and '-' would be excluded, since they can not be in the Hangman game

    return word

def hangman():
    word = get_valid_word(words)
    word_letters=set(word)                  # letters in the word
    alphabet = set(string.ascii_letters)

    used_letters = set()                    # what the user guessed
    lives=6
    while word_letters and lives>0:
        print("Lives ", lives)
        print("You have used these letters: " , " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        # user input
        user_letter = input("Guuess a letter: ").upper()


        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct guess! The letter " , user_letter , " is in the word!")

            else:
                lives = lives - 1
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again! ")


        else:
            print("Invalid character. Please enter a valid character")
            lives -= 1

    if lives==0:
        print("You died, sorry! The word was " , word)
    else:
        print("You guess the word", word , " ! Congrats!")

hangman()