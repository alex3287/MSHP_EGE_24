# ДЕЛ(n, m) => n % m == 0
# not ДЕЛ(n, m) => n % m != 0
# A max
# (ДЕЛ(x, 40) ∨ ДЕЛ(x, 64)) → ДЕЛ(x, A)

def F(x, A):
    return (x % 40 == 0 or x % 64 == 0) <= (x % A == 0)


# for A in range(1, 100):
#     flag = 1
#     for x in range(1, 1000):
#         if F(x, A) == 0:
#             flag = 0
#             break
#     if flag == 1:
#         print(A)

for A in range(1, 100):
    for x in range(1, 1000):
        if F(x, A) == 0:
            break
    else:
        print(A)