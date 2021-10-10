n, w, L = map(int,input().split())
trucks = list(map(int,input().split()))

res = 0
weight = 0
cnt = 0
for i in range(n):
    weight += trucks[0]
    if weight < L:
        trucks.pop(0)
        cnt += 1
    else:
        if weight == L:
            trucks.pop(0)
            cnt += 1
        else:
            if cnt > 1:
                res += cnt + (w-1)
            else:
                res += w
            weight = 0
            cnt = 0
            weight += trucks[0]
            trucks.pop(0)
            cnt += 1

if cnt > 1:
    res += cnt + (w-1) + 1
else:
    res += w + 1
print(res)
