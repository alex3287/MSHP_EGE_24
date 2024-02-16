def alg(N):
    x = N // 1000 + N // 100 % 10
    y = N % 10 + N % 100 // 10
    num = str(max(x, y)) + str(min(x, y))
    return num


# print(alg(3165))
for N in range(1000, 10000):
    R = alg(N)
    if R == '1512':
        print(N, '-> R:', R)