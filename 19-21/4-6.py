# +1 *2   165   1 <= s <= 164

# задача 7
def F(s, pos):
    if s >= 34 and pos == 4: return True
    if s < 34 and pos == 4: return False
    if s >= 34: return False

    if pos % 2 == 0:
        return F(s+1, pos+1) and F(s+2, pos+1) and F(s+3, pos+1) and F(s*2, pos+1)
    return F(s+1, pos+1) or F(s+2, pos+1) or F(s+3, pos+1) or F(s*2, pos+1)

# задача 5
# def F(s, pos):
#     if s >= 65 and s <= 100 and pos == 4: return True
#     if s < 65 and pos == 4: return False
#     if s >= 65: return False
#
#     if pos % 2 == 0:
#         return F(s+1, pos+1) or F(s*3, pos+1)
#     return F(s+1, pos+1) or F(s*3, pos+1)


# задача 6
# def F(s, pos):
#     if s >= 65 and s <= 100 and (pos == 3 or pos == 5): return True
#     if s < 65 and pos == 5: return False
#     if s >= 65: return False
#
#     if pos % 2 == 1:
#         return F(s+1, pos+1) or F(s*3, pos+1)
#     return F(s+1, pos+1)


for s in range(1, 34):
    if F(s, 1):
        print(s)
