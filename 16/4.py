def F(n):
    if n <= 3:
        return n
    if n % 2 == 0:
        return 2 * n + F(n-1)
    return n*n + F(n-2)


count = 0
for n in range(1, 101):
    if F(n) % 3 == 0:
        count += 1
print(count)