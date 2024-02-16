from ipaddress import *


print(2**15 / 4)
# 32768
mask = ip_address('255.255.128.0')
ip = ip_address('212.223.128.1')
#10101010110101 000000000000000
# 
# 13 + 4 = 17
# 13 + 5 = 17
# 13 + 6 = 17
# 13 + 7 = 17
print(255 & 212, 255&223, 128&128, 0&1)
print(int(ip))
# print(int(ip2))
# for i in range(123412, 123456):
#     print()