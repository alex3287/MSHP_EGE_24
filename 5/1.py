def alg(N):
    x1 = N // 1000 + N // 100 % 10
    x2 = N % 10 + N % 100 // 10
    R = str(max(x2, x1)) + str(min(x2, x1))
    # R = f'{max(x2, x1)}{min(x2, x1)}'
    return R


# print(alg(3165))
for N in range(1000, 10000):
    R = alg(N)
    if R == '1311':
        print(f'N:{N} -> R:{R}')