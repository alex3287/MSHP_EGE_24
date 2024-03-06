def F(n):
    if n == 1:
        return 1
    return F(n-1) - 2 * G(n-1)


def G(n):
    if n == 1:
        return 1
    return F(n-1) + G(n-1) + n


print(G(23))