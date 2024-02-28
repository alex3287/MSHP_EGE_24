s = '5' * 500
print(s)
k = 0

while '555' in s or '333' in s:
    if '333' in s:
        s = s.replace('333', '5', 1)
        k += 1
    else:
        s = s.replace('555', '3', 1)

print(s, k)
