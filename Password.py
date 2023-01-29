import random
import string

print("hello, Welcome to DUCITUR password generator")

length = int(input("\ Enter length of of password: "))

lower = ("abcdefghijklmnopqrstuvwxyz")
upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num = string.digits

#sum lower,upper and num

all = lower + upper + num

temp = random.sample(all,length)
password = "".join(temp)

print("Your Password is :",password)