def alg(N):
    # bin_num = f'{N:b}'
    bin_num = bin(N)[2:]
    if N % 3 == 0:
        bin_num += bin_num[-3:]
    else:
        bin_num += bin(N % 3 * 3)[2:]
    R = int(bin_num, 2)
    return R


# print(alg(12))
for N in range(4, 100):
    R = alg(N)
    if 151 < R < 167:
        print(f'N:{N} -> R:{R}')