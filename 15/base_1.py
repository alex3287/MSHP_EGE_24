def F(x, A):
    return ((x % A == 0) and (x % 21 == 0)) <= (x % 18 == 0)

def F(x, A):
    return (x % A != 0) <= ((x % 10 == 0) <= (x % 12 != 0))


for A in range(1, 50):
    flag = 1
    for x in range(1, 1000):
        if F(x, A) == 0:
            flag = 0
            break
    if flag:
        print(A)