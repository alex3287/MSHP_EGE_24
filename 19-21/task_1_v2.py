# +1 *2   165   1 <= s <= 164

# задача 19
# def F(s, pos):
#     if s >= 165 and pos == 3: return True
#     if s < 165 and pos == 3: return False
#     if s >= 165: return False
#
#     if pos % 2 == 1:
#         return F(s+1, pos+1) or F(s*2, pos+1)
#     return F(s+1, pos+1) or F(s*2, pos+1)

# задача 20
# def F(s, pos):
#     if s >= 165 and pos == 4: return True
#     if s < 165 and pos == 4: return False
#     if s >= 165: return False
#
#     if pos % 2 == 0:
#         return F(s+1, pos+1) and F(s*2, pos+1)
#     return F(s+1, pos+1) or F(s*2, pos+1)


# задача 21
def F(s, pos):
    if s >= 165 and (pos == 3 or pos == 5): return True
    if s < 165 and pos == 5: return False
    if s >= 165: return False

    if pos % 2 == 1:
        return F(s+1, pos+1) and F(s*2, pos+1)
    return F(s+1, pos+1) or F(s*2, pos+1)


for s in range(1, 165):
    if F(s, 1):
        print(s)
