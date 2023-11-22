ABC = 'udlr'
count = 0
for a in ABC[1:]:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    word = a + b + c + d + e  # 15*16*16*16*16
                    # print(word, set(word))
                    if word != word[::-1]: # проверка на полиндром
                        count += 1
print(count)

# print(int('A', 16))
# print(ABC.find('G'))
# print(ABC.index('G'))
