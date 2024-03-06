from sys import setrecursionlimit

setrecursionlimit(2500)


def F(n):
    if n == 1:
        return 1
    return n * F(n-1)


print(F(2023) / F(2020))
#F(2023) = 2023 * 2022 * 2021
# print(F(1000))