# 1) 10 -> q        bin, oct, hex
# 2) q -> 10    int(string, base)  ->  int('12343', 7)

# print(int('111', 2))
# print(bin(7)[2:])
# print(f'{7:b}')

ABC = '0123456789ABCDEF'


def ten_to_q(number, base):
    if number < base:
        return ABC[number]
    return ten_to_q(number // base, base) + ABC[number % base]


def ten_to_q2(number, base):
    result = ''
    while number:
        digit = number % base
        result = str(digit) + result  #fixme  result = ABC[digit] + result
        number //= base
    return result


print(ten_to_q(255, 16))
print(ten_to_q2(255, 16))
