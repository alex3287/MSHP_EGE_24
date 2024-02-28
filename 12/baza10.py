from heapq import nsmallest


# def do(string: str) -> str:
#     while "111" in string:
#         string = string.replace("111", "22", 1)
#         string = string.replace("222", "11", 1)
#     return string
#
#
# maps = {}
A = []
for i in range(71, 85):
    s = "1" * i
    print(s, end=' -> ')
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    print(s, s.count('1'), i)
    # A.append(s.count('1'))
    # if s.count('1') == 4:
    #     print(i)
# print(max(A))
#     s = do(s)
#     maps[i] = s.count("1")
#
# max_cnt = max(maps.values())
# for k, v in maps.items():
#     if v == max_cnt:
#         print(k)
#         break


