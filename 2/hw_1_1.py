print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = ((y or z) <= x) or (x == z)
            if not F:
                print(x, y, z)
