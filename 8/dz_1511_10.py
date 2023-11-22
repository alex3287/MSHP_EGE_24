ABC = '01234567'
count = 0
for a in ABC[1:]:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        word = a + b + c + d + e + f  # 15*16*16*16*16
                        # print(word, set(word))
                        if len(set(word)) == 6: # проверка на уникальность каждой цифры
                            # if all(int(word[i], 16) % 2 != int(word[i+1], 16) % 2 for i in range(len(word)-1)):
                            if (int(a) + int(b)) % 2 != 0 and (int(b) + int(c)) % 2 != 0 and \
                                (int(c) + int(d)) % 2 != 0 and (int(d) + int(e)) % 2 != 0 and (int(e) + int(f)) % 2 != 0:
                                    count += 1
                                    # print(word, [int(word[i], 16) % 2 != int(word[i + 1], 16) % 2 for i in range(len(word) - 1)])
print(count)

# print(int('A', 16))
# print(ABC.find('G'))
# print(ABC.index('G'))
