#!/usr/bin/python3
def uppercase(str):
    output = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            output += chr(ord(i) - 32)
        else:
            output += i
    print("{:s}".format(output), end="")
    print()
