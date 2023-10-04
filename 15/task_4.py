def F(x, y, A):
    return (y + 2*x < A) or (x > 20) or (y > 30)


for A in range(1, 100):
    flag = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if F(x, y, A) == 0:
                flag = 0
                break
    if flag == 1:
        print(A)