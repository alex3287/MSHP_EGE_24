alf = "0123456789"
ans = 0
for number in range(1000_000, 10_000_000, 5):
    if len(set(str(number))) == 7:
        # print(number)
        flag = 0
        for i in range(len(str(number)) - 1):
            if int(str(number)[i]) % 2 == int(str(number)[i + 1]) % 2:
                flag = 1
                break

        if flag == 0:
            ans += 1
            # print(f)
print(ans)
# for a in alf:
#     for b in alf:
#         for c in alf:
#             for d in alf:
#                 for e in alf:
#                     for f in alf:
#                         for g in alf:
#                             f = a + b + c + d + e + f + g
#                             if int(f) % 5 == 0:
#                                 if (f.count(a) == 1 and f.count(b) == 1 and f.count(c) == 1 and
#                                         f.count(d) == 1 and f.count(e) == 1 and f.count(f) == 1 and f.count(g) == 1):
#                                     flag = 0
#                                     for i in range(len(f) - 1):
#                                         if (int(f[i]) % 2 == 0 and int(f[i + 1]) % 2 == 0) or (
#                                                 int(f[i]) % 2 == 1 and int(f[i + 1]) % 2 == 1):
#                                             flag = 1
#                                             break
#
#                                     if (flag == 0):
#                                         ans += 1
#                                         print(f)
#                                     print(ans)