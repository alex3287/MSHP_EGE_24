count = 0
ABC = 'КАПН'
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        word = a+b+c+d+e+f
                        if not 'КК' in word and not 'АА' in word and not 'ПП' in word and not 'НН' in word:
                            if word.count('К') == 2 and word.count('А') == 2 and word.count('П') == 1 and word.count('Н') == 1:
                        # if(a != b):
                        #     if(b!=c):
                        #         if(c!=d):
                        #             if(d!=e):
                        #                 if(e!=f):
                        #                     count += 1
                                print(word)
                                count += 1
print(count)
