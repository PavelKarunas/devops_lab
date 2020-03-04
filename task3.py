#!/usr/bin/python3

string = str(input(""))

splitstr = string.split()

words = len(splitstr)

i = 0
finalstr = ''

for i in range(words):
    revword = splitstr[i][::-1] + ' '
    finalstr += revword
print(finalstr)
