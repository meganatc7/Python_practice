from collections import deque

def bfs():
    days = -1
    while ripe:
        days += 1
        for i in range(len(ripe)):
            r, c = ripe.popleft()

            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]

                if 0 <= nr < N and 0 <= nc < M and tomatoBox[nr][nc] == 0:
                    tomatoBox[nr][nc] = 1
                    ripe.append([nr,nc])

    for box in tomatoBox:
        if 0 in box:
            return -1
    return days

M, N = map(int,input().split())
tomatoBox = [list(map(int, input().split())) for _ in range(N)]
dir = [[-1,0],[0,1],[1,0],[0,-1]]

ripe = deque()

for i in range(N):
    for j in range(M):
        if tomatoBox[i][j] == 1:
            ripe.append([i,j])

res = bfs()
print(res)
