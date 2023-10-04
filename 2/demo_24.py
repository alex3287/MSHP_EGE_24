print('x y z w')
for x in 0, 1:
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x and y) == z) and (w)
                if F == 1:
                    print(x, y, z, w)