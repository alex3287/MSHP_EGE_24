ABC = '0234567'
count = 0
for a in '234567':
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    number = a + b + c + d + e
                    if len(set(number)) == 5:
                        # if (int(a)+int(b)) % 2 != 0 and (int(b)+int(c)) % 2 != 0 and (int(c)+int(d)) % 2 != 0 and \
                        # (int(d)+int(e)) % 2 != 0:
                        if all(int(number[i]) % 2 != int(number[i+1]) % 2 for i in range(len(number)-1)):
                            # print(number)
                            count += 1
print(count)

# 72345
