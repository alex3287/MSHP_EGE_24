s = '5'*150
print(s)
while '5555' in s:
    s = s.replace('5555', '33', 1)
    s = s.replace('333', '5', 1)

print(s)
