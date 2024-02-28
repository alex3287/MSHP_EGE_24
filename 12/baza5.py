for n in range(16):
    s = '13'*n + '3'*(15-n)
    k1 = s.count('1')
    # while '13' in s:
    s = s.replace('13', '5')
    suma = sum(int(i) for i in s)
    print(s, '->', suma, '=', k1)

