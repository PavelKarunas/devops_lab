#!/usr/bin/env python


def square_list(N):
    i = 0
    res = []
    if N < 0:
        raise ValueError('Negative number is not allowed')
    while i < N:
        temp = i**2
        res.append(temp)
        i += 1
    return res


if __name__ == "__main__":
    N = int(input())
    result = square_list(N)
    print('\n'.join(map(str, result)))
    result = []
