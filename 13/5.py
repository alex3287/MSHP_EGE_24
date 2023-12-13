from ipaddress import *


ip = ip_address('192.168.32.160')
network = ip_network('192.168.32.160/255.255.255.240')
print(network)
count = 0
for i in network:
    print(bin(int(i))[2:].count('1'))
    if bin(int(i))[2:].count('1') % 2 == 0:
        count += 1
print(count)
