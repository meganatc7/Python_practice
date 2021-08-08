def bfs(a, b):
    q = [(a, b)]
    while q:
        r, c = q.pop(0)
        for d in range(len(dir)):
            nr = r + dir[d][0]
            nc = c + dir[d][1]
            if 0 <= nr < h and 0 <= nc < w and MAP[nr][nc] == 1:
                MAP[nr][nc] = 0
                q.append((nr,nc))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    MAP = []
    for _ in range(h):
        MAP.append(list(map(int, input().split())))

    dir = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    res = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1:
                res += 1
                bfs(i,j)

    print(res)