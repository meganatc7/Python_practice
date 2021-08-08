def change(d, c):
    if c == "L":
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d

def start():
    cnt = 0 # 이동 횟수
    x = 0
    y = 0
    BRD[x][y] = 3
    d = 0
    idx = 0
    info = [] # 뱀 위치 정보
    info.append((x,y))
    while True:
        if direction[idx][0] == cnt:
            d = change(d, direction[idx][1])
            idx += 1
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and BRD[nx][ny] != 3:
            if BRD[nx][ny] == 1:
                BRD[nx][ny] = 3
                info.append((nx,ny))
            elif BRD[nx][ny] == 0:
                BRD[nx][ny] = 3
                info.append((nx,ny))
                ox, oy = info.pop(0)
                BRD[ox][oy] = 0
            x = nx
            y = ny
            cnt += 1
        else:
            cnt += 1
            break
    return cnt


N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수
BRD = [[0] * N for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for _ in range(K):
    r, c = map(int,input().split())
    BRD[r-1][c-1] = 1
L = int(input())
direction = []
for _ in range(L):
    x, c = input().split()
    direction.append([int(x),c])
res = start()

print(res)