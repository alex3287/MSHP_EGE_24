for x in range(16):
    first = f'55{x:x}36'
    second = f'{x:x}2724'
    result = int(first, 19) + int(second, 19)
    print(x, '->', result / 11)