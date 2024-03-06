def F(n):
    if n <3:
        return n+1
    if n>=3 and n%2==0:
        return n +2* F(n +2)
    if n>=3 and n%2!=0:
        return  F(n - 2)+n-2

cnt = 0
for n in range(1, 1001):
    try:
        if len(str(F(n))) == 3:
            cnt += 1
    except:
        pass

print(cnt)