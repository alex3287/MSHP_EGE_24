# Подскажите что у меня за ошибка в№7
def F (n):
    if n > 30:
        return n*n+5*n+4
    if n <= 30 and n % 2 == 0:
        return F(n+1) + 3*F(n+4)
    if n <= 30 and n % 2 != 0:
        return 2*F(n+2) + F(n+5)


def getSum(a):
    suma = 0
    while a != 0:
        suma += a % 10
        a //= 10
    return suma

k = 0

for n in range(1, 1001):
    if getSum(F(n)) == 27:
        k += 1

print(k)