#!/usr/bin/python3

string = str(input("Input str: "))

revstring = string[::-1]

if string.lower() == revstring.lower():
    print("yes")
else:
    print("no")
