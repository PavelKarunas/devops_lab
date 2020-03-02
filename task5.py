#!/usr/bin/python3

num = int(input("Input int: "))

matrix = []
print("Enter the %s x %s matrix: " % (num, num))
for i in range(num):
    matrix.append(list(map(int, input().rstrip().split())))

sum_first_diagonal = sum(matrix[i][i] for i in range(num))
sum_second_diagonal = sum(matrix[i][num - i - 1] for i in range(num))
result = abs(sum_first_diagonal - sum_second_diagonal)
print (result)
