ABC = '0123456789ABCDEFGHTYUIOPL'
# print(len(ABC))


def ten_to_q(number, base):
    if number < base:
        return ABC[number]
    return ten_to_q(number // base, base) + ABC[number % base]


def count_0(number):
    count = 0
    while number:
        digit = number % 25
        if digit == 0:
            count += 1
        number //= 25
    return count


number = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
print(ten_to_q(number, 25))
print(count_0(number))
# 1030