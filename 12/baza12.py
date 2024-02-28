for i in range(50):
    for j in range(50):
        for k in range(50):
            s = '0' + '1' * i + '2' * j + '3' * k + '0'
            res = len(s)
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '320', 1)
                s = s.replace('03', '3012', 1)
            if s.count('1') == 26 and s.count('2') == 54 and s.count('3') == 48:
                print(res)
