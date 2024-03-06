def F(n):
    if n <= 5:
        return n
    if n % 5 == 0:
        return n + F(n/5+1)
    return n + F(n+6)


ans = 0
for i in range(1, 200):
    try:
        r = F(i)
        if r > 1000:
            print(f'i:{i} -> f({i}):{r}')
    except:
        pass