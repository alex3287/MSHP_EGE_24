# def F(x, y, A):
#     return (5*x - 6*y < A) or (x - y > 30)


for A in range(200):
    flag = 1
    for x in range(300):
        for y in range(300):
            F = (5*x - 6*y < A) or (x - y > 30)
            if F == 0:
                flag = 0
                break
    if flag == 1:
        print(A)
