def alg(n):
    n2 = bin(n)[2:]
    if n2.count("1")%2==0:
        n2 += "1"
    else:
        n2 += "0"
    if n2.count("1")%2==0:
        n2 += "1"
    else:
        n2 += "0"
    r = int(n2, 2)
    return r


# print(alg(12))
for N in range(1, 50):
    R = alg(N)
    if R > 54 and R < 57:
        print(R)


def f(n: int) -> int:
  bin_l = list(map(int, list(str(bin(n))[2:])))
  num: str = "".join(map(str, bin_l)) + str(int(sum(bin_l) % 2 == 0)) + str(int(sum(bin_l) % 2 == 0))
  return int(num, 2)

for i in range(0, 1000):
  if f(i) > 54:
    print(i, f(i))
    break