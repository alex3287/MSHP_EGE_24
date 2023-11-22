ABC = 'КАЛИЙ'
count = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    word = a + b + c + d + e
                    if len(set(word)) == 5 and a not in 'Й' and word.count('ИА') == 0:
                        count += 1
                        print(word)
print(count)