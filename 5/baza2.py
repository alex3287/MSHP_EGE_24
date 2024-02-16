a = 999
output = 0

while output != "815":
    a += 1
    interim1 = a // 10 % 10 + a // 10 // 10 % 10
    interim2 = a % 10 + a // 10 // 10 // 10
    output = str(min(interim1, interim2)) + str(max(interim2, interim1))

print(a)