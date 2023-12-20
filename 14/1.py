for base in range(5, 20):
    first = int('144', base)
    second = int('24', base)
    third = int('201', base)
    if first + second == third:
        print(f'{base} -> {first}+{second}={third}')