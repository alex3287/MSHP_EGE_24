def F(x, y, z, w):
    return (x <= y) and not (y == z) and (w <= x)


print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = F(x, y, z, w)
                if f:
                    print(x, y, z, w)