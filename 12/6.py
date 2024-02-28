# s = '>' + '1'*28 + '2'*18 + '3'*35
s = '>' + '2'*10 + '3'*20 + '1'*14 + '2'*8 + '3'*15 + '1'*14
print(s)

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>1', 1)
    if '>3' in s:
        s = s.replace('>3', '1>2', 1)

print(s)
print(s.count('2')*2 + s.count('1'))
suma = sum(int(i) for i in s[:-1])
suma2 = sum(list(map(int, s[:-1])))
print(suma, suma2)
