W, H = map(int,input().split())
N = int(input())
block = [[0] * (W+1) for _ in range(H+1)]
k = 0
for n in range(1,N+2):
    a, b = map(int,input().split())
    k += 1
    if b == 0:
        k -= 1
        continue
    if a == 1:
        block[0][b] = k
        player = [0,b]
    elif a == 2:
        block[H][b] = k
        player = [H, b]
    elif a == 3:
        block[b][0] = k
        player = [b,0]
    elif a == 4:
        block[b][W] = k
        player = [b,W]
r = player[0]
c = player[1]


dir = 0
if a == 1:
    dir = 2
elif a == 2:
    dir = 0
elif a == 3:
    dir = 1
elif a == 4:
    dir = 3
# 시계방향 거리 구하기
dc = [-1,0,1,0] # 시계
dr = [0,-1,0,1] # 시계
clock = []
for i in range(1,N+1):
    nr = r
    nc = c
    cnt = 0
    d = dir
    while block[nr][nc] != i:
        nr += dr[d]
        nc += dc[d]
        cnt += 1
        if nr < 0 or nr > H or nc < 0 or nc > W:
            nr -= dr[d]
            nc -= dc[d]
            cnt -= 1
            d = (d + 1) % 4
    clock.append(cnt)

dir = 0
if a == 1:
    dir = 0
elif a == 2:
    dir = 2
elif a == 3:
    dir = 1
elif a == 4:
    dir = 3
# 반시계방향 거리 구하기
dc = [-1,0,1,0] # 반시계
dr = [0,1,0,-1] # 반시계
r_clock = []
for i in range(1,N+1):
    nr = r
    nc = c
    cnt = 0
    d = dir
    while block[nr][nc] != i:
        nr += dr[d]
        nc += dc[d]
        cnt += 1
        if nr < 0 or nr > H or nc < 0 or nc > W:
            nr -= dr[d]
            nc -= dc[d]
            cnt -= 1
            d = (d + 1) % 4
    r_clock.append(cnt)

result = 0
for i in range(len(clock)):
    if clock[i] <= r_clock[i]:
        result += clock[i]
    else:
        result += r_clock[i]

print(result)