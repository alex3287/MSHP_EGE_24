ABC = 'ЛЕТО'
count = 0
for a in 'ЛТ':
    for b in ABC:
        for c in ABC:
            for d in ABC:
                word = a + b + c + d
                count += 1
                print(word)
print(count)