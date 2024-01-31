# +2 *2   231      s1=17   1 <= s2 <= 213

def win_1(s1, s2):
    return s1+2 + s2 >= 231 or s1*2 + s2 >= 231 or s1 + s2+2 >= 231 or s1 + s2*2 >= 231
# 107 - 213


def win_2(s1, s2):
    return not(win_1(s1, s2)) and win_1(s1+2, s2) and win_1(s1*2, s2) and win_1(s1, s2+2) and win_1(s1, s2*2)
# 211


def win_3(s1, s2):
    return win_2(s1+2, s2) or win_2(s1*2, s2) or win_2(s1, s2+2) or win_2(s1, s2*2)


def win_4(s1, s2):
    return win_1(s1, s2*2) and win_3(s1*2, s2) and win_3(s1, s2+2) and win_3(s1+2, s2) or \
        win_1(s1*2, s2) and win_3(s1, s2+2) and win_3(s1, s2 * 2) and win_3(s1 + 2, s2)


for s2 in range(1, 214):
    if win_4(17, s2):
        print(s2)