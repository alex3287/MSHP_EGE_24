from ipaddress import *


network = ip_network('117.32.0.0/255.224.0.0')
count = 0
for i in network:
    s = str(i)
    A = [int(i) for i in s.split('.')]
    suma = A.count(A[0]) + A.count(A[1]) + A.count(A[2]) + A.count(A[3])
    if suma == 6:
        count += 1
        print(A) # 125.5.255.123
print(count)
# 117 32