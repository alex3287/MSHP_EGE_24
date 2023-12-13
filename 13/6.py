from ipaddress import *


network = ip_network('202.75.38.160/255.255.255.240')
count = 0
for i in network:
    print(bin(int(i))[2:])
    if bin(int(i))[2:].count('111') != 0:
        count += 1
        # print(bin(int(i))[2:])
print(count)

s = '01111101100010101'
print(s.count('111'))