#!/usr/bin/python3

num = int(input("Input int: "))

num2 = num
digits = ()

for i in range(9, 1, -1):

    while (num % i == 0):

        num = num // i

if (num != 1):
    print(-1)
    exit()

x = 10
while True:
    y = [int(a) for a in str(x)]
    product = 1
    for z in y:
        product *= z
    if product == num2:
        break
    else:
        x += 1
print(x)
