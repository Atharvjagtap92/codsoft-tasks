##### PASSWORD MAKING TASK #####

import string
import random

if __name__ == "__main__":
    #print(s1)it contain lowercase alphabet.
    s1 = string.ascii_lowercase
    #print(s2)it contain uppercase alphabet.
    s2 = string.ascii_uppercase
    #print(s3)it contain all the digits(0to9).
    s3 = string.digits
    #print(s4)it contain all the punctuation character.
    s4 = string.punctuation
    
    try:
        plen = int(input("Enter password length\n"))
    except ValueError:
        print("Please enter a valid integer for the password length.")
        exit()
    
    if plen < 1:
        print("Password length must be at least 1.")
        exit()
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    
    print("Your password is:")
    print("".join(s[0:plen]))
