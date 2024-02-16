# +2 *2   231      s1=17   1 <= s2 <= 213

# задача 19
def F(s1, s2, pos):
    if s1+s2 >= 231 and pos == 3: return True
    if s1+s2 < 231 and pos == 3: return False
    if s1+s2 >= 231: return False
    if pos % 2 == 1:
        return F(s1+2, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*2, pos+1)
    return F(s1+2, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*2, pos+1)
# 17 + 211 (228 + 2 = 230) ==>> 211


# задача 20
# def F(s1, s2, pos):
#     if s1+s2 >= 231 and pos == 4: return True
#     if s1+s2 < 231 and pos == 4: return False
#     if s1+s2 >= 231: return False
#     if pos % 2 == 0:
#         return F(s1+2, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+2, pos+1) and F(s1, s2*2, pos+1)
#     return F(s1+2, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*2, pos+1)
# 53, 98, 104, 105


# задача 21
# def F(s1, s2, pos):
#     if s1+s2 >= 231 and (pos == 3 or pos == 5): return True
#     if s1+s2 < 231 and pos == 5: return False
#     if s1+s2 >= 231: return False
#     if pos % 2 == 1:
#         return F(s1+2, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+2, pos+1) and F(s1, s2*2, pos+1)
#     return F(s1+2, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+2, pos+1) or F(s1, s2*2, pos+1)
# 96 103 106


for s2 in range(1, 214):
    if F(17, s2, 1):
        print(s2)
