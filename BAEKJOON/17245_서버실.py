def computer(m):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if m <= serverRoom[i][j]:
                cnt += m
            else:
                cnt += serverRoom[i][j]
    return cnt

N = int(input())
serverRoom = []
maxV, sumV = 0, 0
for n in range(N):
    tmp = list(map(int, input().split()))
    serverRoom.append(tmp)
    maxV = max(maxV, max(tmp))
    sumV += sum(tmp)

s, e = 0, maxV
res = 0
while s <= e:
    m = (s + e) // 2
    if computer(m) >= (sumV / 2):
        res = m
        e = m-1
    else:
        s = m+1
print(res)