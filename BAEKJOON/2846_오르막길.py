N = int(input())
road = list(map(int,input().split()))

tmp = 0
maxV = 0

for i in range(1,N):
    slope = road[i] - road[i-1]
    if slope >= 1:
        tmp += slope
    else:
        tmp = 0

    if maxV < tmp:
        maxV = tmp

print(maxV)