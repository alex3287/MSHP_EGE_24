ABC = 'АЙСБЕРГ'
count = 0
for a in 'АСБЕРГ':
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        for g in ABC:
                            word = a + b + c + d + e + f + g
                            if len(set(word)) == 7 and word.count('ЙА') == 0 and word.count('ЙЕ') == 0:
                                count += 1
                                print(word)
print(count)