ABC = '01234'


def ten_to_q(number, base):
    if number < base:
        return ABC[number]
    return ten_to_q(number // base, base) + ABC[number % base]


A = []
for i in range(16):
    num_16 = f'e{i:x}'
    num_10 = int(num_16, 16)
    num_2 = bin(num_10)
    num_8 = oct(num_10)
    if num_8[-2] == '5' and num_2[-3] == '1':
        print(num_2, num_8, num_10, num_16)
        A.append(num_10)

print(A)

for i in A:
    print(ten_to_q(i, 4))