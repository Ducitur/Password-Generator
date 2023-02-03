import random
import string

#ne stand for name
ne = input('What is your name:\n')


print('Hello' +" " + ne + "\nWelcome to DUCITUR password generator\n")

print("NOTE: your password length must be above 7\n")

#loop line 10 until condition is fulfill
while True:
    length = int(input('Enter length of password: '))

    if length < 7:
        continue

    lower = ('abcdefghijklmnopqrstuvwxyz')
    upper = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sum = string.digits
    signs = string.punctuation

    #add the following variable lower,upper,sum and signs(all)

    all = lower + upper + sum + signs

    #create a variable to hold the variable called temp

    temp = random.sample(all, length)
    password = "".join(temp)
    print("Your Password is :",password)
    break 

print("\nYour security is our top priority")

print("\nThanks for using DUCITUR password generator")
