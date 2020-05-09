# password generator with regex 
# PASSWORD SHOULD BE MINIMUM OF 6 CHARACTERS LONG 
# PASSWORD SHOULD HAS MINIMUM 2 LETTERS 
# PASSWORD SHOULD HAS MINIMUM 2 NUMBER 
# PASSWORD SHOULD HAS MINIMUM 2 CHARACTERS EXCEPT SPACE 
# ASK HOW MANY LETTERS USER WANT TO 
# ASK HOW MANY NUMBERS USER WANT TO

# MAIN PROGRAM
# 1. PASSWORD GENERATOR
# 2. PASSWORD CHECKER
# 3. EXIT

# PASSWORD GENERATOR
# 1. GET HOW MANY LETTERS USER WANT TO ---> MIN=2, IF LESS TRY AGAIN
# 2. GET HOW MANY NUMBERS USER WANT TO ---> MIN=2, IF LESS TRY AGAIN
# 3. GET HOW MANY CHARACTERS USER WANT TO --> MIN=2, IF LESS TRY AGAIN
# 4. FUNCTION GENERATEPASSWORD() WILL GENERATE PASSWORD
# 5. COPY PASSWORD TO THE CLIPBOARD AND PRINT INFORMATION

# PASSWORD CHECKER
# 1. GET THE PASSWORD FROM THE USER
# 2. CHECK IF IT IS STRONG
# 3. PRINT RESULT

def generatePassword(lettersAmount, numbersAmount, charactersAmount):
    password = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'U', 'P', 'R', 'S', 'T', 'W', 'Y', 'Z', 'X', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '[', '{', ']', '}', ';', ':', '"', '\'', '|', '\\', ',', '<', '.', '>', '?', '/']
    # Adding letters
    for i in range(lettersAmount):
        password.append(letters[random.randint(0, len(letters))])
    for i in range(numbersAmount):
        password.append(numbers[random.randint(0, len(numbers))])
    for i in range(charactersAmount):
        password.append(characters[random.randint(0, len(characters))])
    random.shuffle(password)
    passwordFinal = ''.join(password)
    pyperclip.copy(passwordFinal)
    print('Password copied to the clipboard')

def passwordChecker():
    # this function will return False if password is weak
    passwordStrong = False
    password = pyip.inputPassword('Enter your password: ')
    # checking numbers
    numbersRegex = re.compile(r'\d')
    if len(numbersRegex.findall(password)) < 2:
        return passwordStrong
    # checking letters 
    lettersRegex = re.compile(r'[a-zA-Z]')
    if len(lettersRegex.findall(password)) < 2:
        return passwordStrong
    # checking characters 
    charactersRegex = re.compile(r'[!@#$%&*()_-+={}:;"<,>./?|\]') #HERE there is some bug, check python regex documentation and fix it
    if len(charactersRegex.findall(password)) < 2:
        return passwordStrong
    passwordStrong = True
    return passwordStrong



# MAIN PROGRAM
# IMPORTING MODULES
import re
import random
import pyinputplus as pyip
import pyperclip

inputMenu = 'ok' 

while inputMenu != 'EXIT' and inputMenu != '3':
    inputMenu = pyip.inputChoice(['1', '2', '3', 'PASSWORD GENERATOR', 'PASSWORD CHECKER', 'EXIT'], '1. PASSWORD GENERATOR\n2. PASSWORD CHECKER\n3. EXIT\n')
    if inputMenu == 'PASSWORD GENERATOR' or inputMenu == '1':
        # PASSWORD GENERATOR
        print('PASSWORD GENERATOR')
        lettersAmount = pyip.inputInt('How many letters would you like? ', min=2)
        numbersAmount = pyip.inputInt('How many numbers would you like? ', min=2)
        charactersAmount = pyip.inputInt('How many characters would you like?', min=2)
        generatePassword(lettersAmount, numbersAmount, charactersAmount)
    elif inputMenu == 'PASSWORD CHECKER' or inputMenu == '2':
        # PASSWORD CHECKER
        print(passwordChecker())
        print('blabla')
