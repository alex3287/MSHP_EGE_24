def F(x, A):
    return ((x & 20 != 0) or (x & 55 != 0)) <= ((x & 7 == 0) <= (x & A != 0))


for A in range(1, 70):
    for x in range(1, 1000):
        if not F(x, A):
           break
    else:
        print(A)