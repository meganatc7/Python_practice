S, C = map(int,input().split())
pa = []
maxV = 0
for _ in range(S):
    tmp = int(input())
    maxV = max(maxV, tmp)
    pa.append(tmp)

sumV = sum(pa)

s, e = 1, maxV

while s <= e:
    mid = (s + e) // 2

    cnt = 0
    for i in range(S):
        cnt += pa[i] // mid

    if cnt >= C:
        s = mid + 1
    else:
        e = mid - 1

cnt = 0
res = 0
for p in pa:
    cnt += p // e
    res += p % e

res += (cnt - C) * e

print(res)