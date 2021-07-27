N  = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

cost = 0
tmp = 0
minV = oil[0]
for i in range(N):
    if i == N-1:
        cost += (tmp * minV)
        print(cost)
    else:
        if oil[i] < minV:
            cost += (tmp * minV)
            tmp = 0
            minV = oil[i]
        tmp += road[i]