def alg(n):
    p1 = n // 1000 + n // 100 % 10
    p2 = n // 100 % 10 + n % 100 // 10
    p3 = n % 10 + n % 100 // 10
    sum = p1 + p2 + p3
    # mini = min(p1,p2,p3)
    midp = sum - max(p1, p2, p3) - min(p1, p2, p3)
    maxp = max(p1, p2, p3)
    res = str(max(midp, maxp)) + str(min(midp, maxp))
    return res

# print(alg(1284))
for n in range(1000, 10000):
    res = alg(n)
    if res == '1414':
        print(f'N:{n} => R:{res}')