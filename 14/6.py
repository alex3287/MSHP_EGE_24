ABC = '0123456789ABCDEF'


def ten_to_q(number, base):
    if number < base:
        return ABC[number]
    return ten_to_q(number // base, base) + ABC[number % base]


number = 3**3 * 7**69 - 70
result = ten_to_q(number, 7)

# нахождение суммы цифр в строке
suma = result.count('6')*6  # 413
suma2 = sum(int(i) for i in result)
suma3 = sum(map(int, result))

print(suma, suma2, suma3)