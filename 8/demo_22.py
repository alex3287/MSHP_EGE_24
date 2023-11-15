ABC = 'ЕЛМРУ'
count = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                word = a + b + c + d
                count += 1
                if a == 'Л':
                    print(count, word)
