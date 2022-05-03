# Random Password Generator
# Author: Aramis Valdes
# This simple password generator uses a text file as a dictionary to generate easy to remember passwords.

# importing Used Modules
from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import choice, randint

# Checks if word list is downloaded, and downloads it if not.
if not isfile('words.txt'):
    print("Downloading Wordlist ...")
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    with open("Words.txt", "wb") as f:
        f.write(urlopen(url).read())

# Variable
# Opens, Reads, and splits file into list.
words = open("words.txt", "r").read().split("\n")
special_chars = ["!", "?", "@", "%", "+", "/", "#", "$"]


# This function generates the password with the parameters entered by the user.
def create_password(num_words, num_numbers, num_special):
    pass_str = ""

    for _ in range(num_words):
        pass_str += choice(words).lower().capitalize()
    for _ in range(num_numbers):
        pass_str += str(randint(0, 9))
    for _ in range(num_special):
        pass_str += choice(special_chars)
    return pass_str


# defines the main function of the program
def main():
    # Ask user for input to be used by the create_password function.
    num_words = int(input('\nEnter the length of words in password: '))
    num_numbers = int(input('\nEnter the length of numbers in password: '))
    num_special = int(input('\nEnter the length of special characters in password: '))

    # Passes input into the create_password function and prints out the generated password.
    pass_str = create_password(num_words, num_numbers, num_special)
    strength, _ = test(pass_str)
    print("\n\nPassword: %s" % pass_str)  # prints out the randomly generated password.
    print(
        "Strength: %0.5f" % strength)  # prints out the strength of the password according to the password meter library.


if __name__ == "__main__":
    main()
