import random
import string

#ask user for min length of password
#ask if user wants special characters (#$%...)

def generate_password(min_length, numbers=True, special_characters=True):
    
    
    letters = string.ascii_letters      #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits              #0123456789
    special_chars = string.punctuation  #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    
    password_chars = letters #always include letters
    if numbers :
        password_chars += digits
    if special_characters :
        password_chars += special_chars
        
    
    
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(password) < min_length:
        #add one char to the password string
        new_char = random.choice(password_chars)
        password += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special = True
            
        meets_criteria = True               #make it true and then try to prove it false
        if numbers:                         #false if supposed to have numbers but doesn't have any
            meets_criteria = has_number
        if special_characters:              #false if supposed to have special chars but either failed before (meets_criteria is already False) or doesn't have special chars
            meets_criteria = meets_criteria and has_special
    return password



min_length = int(input("What is the password minimal length?\n"))
numbers = input("Whould you like to have numbers in it (y/n) ?\n").lower() == "y" #checks if user input is lowercase y and stores the boolean
special_chars = input("Would you like to have special chars in it (y/n) ?\n").lower() =="y"
variants_number = int(input("How many variants of passwords would you like ?\n"))


passwords_generated = 0
while passwords_generated < variants_number:
    password = generate_password(min_length, numbers, special_chars)
    print(password, "\n")
    passwords_generated +=1
