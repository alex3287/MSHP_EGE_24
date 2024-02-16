def alg(N):
    # bin_num = f'{N:b}'
    bin_num = bin(N)[2:]
    if bin_num.count('1') % 2 == 0:
        bin_num += '0'
    else:
        bin_num += '1'

    if bin_num.count('1') % 2 == 0:
        bin_num += '0'
    else:
        bin_num += '1'
    R = int(bin_num, 2)
    return R


# print(alg(12))
for N in range(4, 50):
    R = alg(N)
    if R > 108:
        print(f'N:{N} -> R:{R}')