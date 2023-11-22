ABC = '0123456789ABCDEF'
count = 0
for a in ABC[1:]:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    word = a + b + c + d + e  # 15*16*16*16*16
                    # print(word, set(word))
                    if len(set(word)) == 5: # проверка на уникальность каждой цифры
                        # if all(int(word[i], 16) % 2 != int(word[i+1], 16) % 2 for i in range(len(word)-1)):
                        if (int(a, 16) + int(b, 16)) % 2 != 0 and (int(b, 16) + int(c, 16)) % 2 != 0 and \
                            (int(c, 16) + int(d, 16)) % 2 != 0 and (int(d, 16) + int(e, 16)) % 2 != 0:
                                count += 1
                                # print(word, [int(word[i], 16) % 2 != int(word[i + 1], 16) % 2 for i in range(len(word) - 1)])
print(count)

# print(int('A', 16))
# print(ABC.find('G'))
# print(ABC.index('G'))
