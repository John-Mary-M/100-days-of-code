#!/usr/bin/python3
#2/06/2023 random password generator

'''
Password length is determined by the user
Password should involve atleast one digit, one Upper case, one lowercase,
and at least one speacial character.
'''
import random
import string

def main():
    passLen = input('How long do you want your password to be?\n')
    passLen = int(passLen)
    generate_password(passLen)

def generate_password(x):
    upperCase = string.ascii_uppercase
    lowerCase = string.ascii_lowercase
    nums = string.digits
    specialXters = string.punctuation

    #combine all characters into one list
    all_xters = upperCase + lowerCase + nums + specialXters

    password = ''
    #generate the password using a loop to step through the xters
    for i in range(x):
        password += random.choice(all_xters)

    #make the pasword more secure by shuffling the xters
    password_list = list(password) #typecast the password into a list
    random.shuffle(password_list) #shuffle the list
    password = ''.join(password_list)

    print(password)

if __name__ == '__main__':main()
