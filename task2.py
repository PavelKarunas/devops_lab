#!/usr/bin/python3

string = str(input("Input str: "))

length = len(string)

revstring = string[length::-1]

if string.lower() == revstring.lower():
    print("yes")
else:
    print("no")
