def F(x, A):
    return (x & 56 != 0) <= ((x & 48 == 0) <= (x & A != 0))


for A in range(1, 100):
    flag = 1
    for x in range(1, 1000):
        if F(x, A) == 0:
            flag = 0
            break
    if flag == 1:
        print(A)