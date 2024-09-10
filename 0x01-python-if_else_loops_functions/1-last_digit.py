#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = 0
if number < 0:
    number *= -1
    i = 1
ld = number % 10
if i == 1:
    number *= -1
    ld *= -1
print("Last digit of {:d} is ".format(number), end="")
if ld > 5:
    print("{:d} and is greater than 5".format(ld))
elif ld == 0:
    print("{:d} and is 0".format(ld))
else:
    print("{:d} and is less than 6 and not 0".format(ld))
