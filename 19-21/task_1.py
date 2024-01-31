# +1 *2   165   1 <= s <=164
# 19 победа Вани, при любом ходе Пети

def win_1(s):
    return s+1 >= 165 or s*2 >= 165
# 83 - 164


def win_2(s):
    return not(win_1(s)) and win_1(s+1) and win_1(s*2)
# 82


def win_3(s):
    return win_2(s+1) or win_2(s*2)
# 41 81


def win_4(s):
    return win_1(s*2) and win_3(s+1) or win_1(s+1) and win_3(s*2)
# 80


for s in range(1, 165):
    if win_4(s):
        print(s)