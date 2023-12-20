for x in range(12):
    first = f'19{x:x}61'
    second = f'3393{x:x}'
    third = f'60{x:x}05'
    if int(first, 12) + int(second, 17) == int(third, 15):
        print(x, int(third, 15))